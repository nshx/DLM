## DESCRIPTION
### Algorithmes de capture et traitements des flux vidéos.</br>
Ces algorithmes ont pour objectif de monitorer l'avant et l'arrière d'un véhicule en mouvement, à la recherche d'éventuelles dangers/obstacles et/ou informations qui doivent impérativement être retranscrite au conducteur. Ainsi, le programme principal (multiple_video_flux ou single_video_flux) instancie 3 niveaux de criticité :</br>
<ul>
  - <strong>Information</strong> -> Evenement dont le danger est proche de 0 mais qui pourrait dans l'avenir être une menace (exemple: pieton au loin).</br>
  - <strong>Warning</strong> -> Evénement qui sucite une action de la part de l'utilisateur dans les plus brefs délais (exemple: feu orange - ralentir en vue de s'arrêter).</br>
  - <strong>Danger</strong> -> Evénement dont l'accident est quasi inevitable sans l'action autonome du véhicule (exemple: Piéton à une distance d'arrêt limite, le véhicule entreprend l'arrêt d'urgence par lui-même [ ce stade ne s'enclenche que si le "warning" a déjà été lancé préalablement et qu'aucune réponse de l'utilisateur ne soit servenu ].</br>
</ul>

## Livrable
Dans le dossier décompressé src.zip, vous trouverez l'arborescence suivante :
```
    assets                              => Fichier contenant l'ensemble des images qui ont servi aux tests des algorithmes.
        image.png                       => Image de 3 feux tricolores dont l'un est renversé
        Rouge.png                       => Image d'un feu rouge actif
        Vert.png                        => Image d'un feu vert actif
    Single_Video_Flux.py                => Code source pour la gestion d'un unique flux vidéo par usb
    Multiple_Video_Flux.py              => Code source pour la gestion d'une multitude de flux vidéo par usb - (ici, nous n'utiliserons que 2 flux)
    Traffic_Light_Detection.py          => Code source de détection de feux tricolores par comparaisons de formes et de couleurs
    Object_Detection.py                 => Code source basé sur une intelligence artificielle pré-entraînée
    MobileNetSSD_deploy.caffemodel      => Fichier model sur lequel se base l'IA
    MobileNetSSD_deploy.protoxtxt.txt   => Défini l'architecture du model
    Color_Detection.py                  => Code source pour la détection de couleurs avec masques dans l'espace HSV
    Line_Detection.py                   => Code source pour la détection de ligne droite
``` 
src: Algorithme de détection de feux tricolores terminé ainsi que celui pour la détection d'objet.</br>

## Installation
Télécharger puis décompresser le fichier WebApp_V6.zip.</br>

## Application WEB
Ouvrir le dossier "WebApp_V6".</br>
Double-cliquez sur le fichier "page.html".</br>

### Fonctionnement de la page WEB [Onglet "MAP"]
#### Mode Simulation : Définir les niveaux des signaux RSSI.</br>
Dans les espaces d'édition de texte (B1 à B3), l'utilisateur à la possibilité de modifier les valeurs par défaut [-120].</br>
Les valeurs autorisées sont comprises entre -120 jusqu'à -30 dbm. Elles correspondant au niveau de puissance qu'un module HC-05 peut émettre.</br>
<strong>-30</strong> est le signal le plus fort que le module puisse émettre, ce qui signifie que l'utilisateur se positionne à moins d'1m de la balise.</br>
<strong>-120</strong> est le signal le plus faible correspondant à une distance utilisateur-balise d'environ 10m moyennant les problèmes de propagation dûs à l'environnement où se trouve les deux entités.</br>
Pour réaliser la fonction de triangulation présentée ci-après, j'ai procédé par tests pour déterminer la distance correspondant à un niveau RSSI.</br>
Les données résultantes de la distance en fonction du signal reçu sont écrites ci-dessous:</br>

<ul>
  <pre>
<strong>[dBm]        [m]</strong></br>
 -30         1</br>
 -40         2</br>
 -50         3</br>
 -60         4</br>
 -70         5</br>
 -80         6</br>
 -90         7</br>
 -100        8</br>
 -110        9</br>
 -120        10
   </pre>
</ul>

Si l'utilisateur ne donne pas un multiple de 10, alors la valeur qui sera retournée par la fonction de triangulation est la moyenne des bornes supérieure et inférieure.</br> (Exemple: <strong>input</strong> = -34 dBm; </br> &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp; &nbsp;  &nbsp; <strong>output</strong> = (-30 dBm) + (-40 dBm) / 2 -> (1 m + 2 m) / 2 = 1.5m)</br>

Une fois les valeurs RSSI entrées pour chaque balise, l'utilisateur peut lancer la localisation avec le bouton "scan-area".

#### Mode Simulation : La Triangulation.</br>
_Note: Toutes les données sont des approximations. Puisque la simulation ne vérifie pas que les RSSI concordent entre eux, il y a également une approximation sur ces données._</br>
Il existe quatre cas de figure:
<ul>
  - Aucune balise detecté,</br>
  - Une balise detecté,</br>
  - Deux balises detectés,</br>
  - Trois balises detectés.</br>
</ul>
Chaque cas est determiné par le RSSI des 3 balises.

Si le RSSI est supérieur à -30 dBm (alors il y'a une erreur donc RSSI = 0) et si rssi est inférieur à -120 dBm (même opération, RSSI = 0)
Lorsque le rssi d'une balise vaut 0 son signal n'existe pas et le nombre de balise detecté diminue de 1.

##### Traitement du cas 1: Zéro balise detectée </br>
Rien n'est mis à jour, le système reste dans sa dernière position connue.</br>

##### Traitement du cas 2: Une balise detectée </br>
L'utilisateur se place directement au-dessus de la balise dont le signal est capté.</br>
Cette approximation est obligatoire étant donné l'infinité de possibilités (l'utilisateur peut être n'importe où dans la zone de la balise).</br>

##### Traitement du cas 3: Deux balises detectées </br>
Détection des intersections des deux zones (cercles verts fluorescents).</br>
L'utilisateur se placera au centre de la droite qui lie les deux intersections.</br>

##### Traitement du cas 4: Trois balises detectées </br>
Détection des intersections des trois zones (cercles verts fluorescents).</br>
L'utilisateur se placera au centre du triangle formé par les trois intersections.</br>

## Serveur-WebAPP (en coordination avec Félix)
Avant de démarrer l'application (double click sur le fichier page.html),</br>
il faut vérifier l'adresse IP du serveur de l'API/Database (127.0.0.1 pour un test en local ou l'IP de la raspberry)</br>
Pour s'assurer de la récupération des données, nous regardons la console DevTools (touche F12) de la page Web.</br>
![setflag](https://user-images.githubusercontent.com/92402906/143230502-82cc5493-3866-4f65-9338-8d064d4c5c6a.jpg)</br>
Par défaut (et pour faciliter les tests), le drapeau est initialisé à 1.</br>
C'est pourquoi au lancement de la page web, nous récupérons les données stockées dans la database.</br>
L'application Web check toutes les 5 secondes l'état du drapeau :</br>
S'il est à 1, elle lance une requête GET pour récupérer les données des 3 balises.</br>
Elle lance une requête PUT pour reset la valeur du drapeau à 0.</br>
Nous simulons manuellement la mise à jour de nouvelles valeurs avec la commandes cURL PUT présentée précédemment.</br>
Pour indiquer l'état READ READY à l'application web, nous passons la valeur du drapeau à 1 : depuis un terminal Linux :
```
curl -X PUT -H "Content-Type: application/json" -d '{"flag":1}' http://localhost:3000/api/v3/beacons/0/
```
Une fois le drapeau à jour, l'application Web relance une requête GET (après 38 essais sur la capture d'écran) pour récupérer les données des 3 balises.</br>

## Application Android
Le téléphone scan et recherche les balises du réseau grâce à leur adresse BT unique.</br>
Il récupère jusqu'à 3 RSSI puis envoie une requête PUT pour mettre à jour la database</br>
et passer le drapeau à 1.</br>

## Updates :
&nbsp;&nbsp;&nbsp;- 07/12/2021: Version 6.0.0, Alexandre LEPERS (lepers199)

## References
Création page HTML/CSS: https://www.youtube.com/watch?v=oYRda7UtuhA&ab_channel=EasyTutorials</br>
Canvas JavaScript: https://developer.mozilla.org/fr/docs/Web/HTML/Element/canvas</br>
Gradient Javascript: https://www.w3schools.com/html/html5_canvas.asp</br>
Iteration dict JavaScript: https://stackoverflow.com/questions/34913675/how-to-iterate-keys-values-in-javascript</br>
JavaScript to HTML: https://openclassrooms.com/forum/sujet/passer-une-variable-js-a-un-code-html
