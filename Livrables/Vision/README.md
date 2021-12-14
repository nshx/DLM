## DESCRIPTION
### Algorithmes de capture et traitements des flux vidéos</br>
Ces algorithmes ont pour objectif de monitorer l'avant et l'arrière d'un véhicule en mouvement, à la recherche d'éventuelles dangers/obstacles et/ou informations qui doivent impérativement être retranscrite au conducteur. Ainsi, le programme principal (multiple_video_flux ou single_video_flux) instancie 3 niveaux de criticité pour chaque éléments qu'il peut détecter.</br>

#### Niveaux de criticité</br>
<ul>
  - <strong>Information</strong> -> Evénement dont le danger est proche de 0 mais qui pourrait dans l'avenir être une menace (exemple: pieton au loin ou panneaux limitation de vitesse 50 km/h).</br>
  - <strong>Warning</strong> -> Evénement qui sucite une action de la part de l'utilisateur dans les plus brefs délais (exemple: feu orange - ralentir en vue de s'arrêter).</br>
  - <strong>Danger</strong> -> Evénement dont l'accident est quasi inevitable sans l'action autonome du véhicule (exemple: Piéton à une distance d'arrêt limite, le véhicule entreprend l'arrêt d'urgence par lui-même [ ce stade ne s'enclenche que si le "warning" a déjà été lancé préalablement et qu'aucune réponse de l'utilisateur ne soit servenu ].</br>
</ul>

#### Eléments détectable</br>
<ul>
  - Feux tricolores</br>
  - Personnes</br>
  - Voitures</br>
  - Bus</br>
  - Motos</br>
  - Voitures</br>
  - Chats</br>
  - Chiens</br>
  - Chevaux</br>
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
Fichier src: _Algorithme de détection de feux tricolores terminé ainsi que celui pour la détection d'objets._</br>

## Installation
Télécharger puis décompresser le fichier src.zip.</br>
### Dépendances Python</br>
<ul>
  - python v.3.8.x </br>
  - opencv-python v.4.5.4.58 </br>
  - numpy v.1.20.1 </br>
  - threading </br>
</ul>

## Run Application
Dans une invite de commande, déplacez-vous jusqu'à l'emplacement des codes sources python.</br>
### WINDOWS:
  > python Single_Video_Flux.py</br>
ou</br>
  > python Multiple_Video_Flux.py</br>
### LINUX:
 > ./Single_Video_Flux.py</br>
ou</br>
  > ./Multiple_Video_Flux.py</br>

## Fonctionnement des différents algorithmes 
### Single_Flux_Video & Multiple_Flux_Video</br>
<ul>
> class camThread() => Permet de créer des objets caméras pour instancier un flux vidéo depuis n'importe quel port USB voulu. La classe utile les threads pour séprarer les flux de chaque caméras sur des canaux bien distinct.</br>

    > La fonction principale qui est appelée par l'objet caméra dans son thread s'appelle camPreview().</br>
    Cette fonction permet d'initialiser les paramètres du flux vidéo, de récupérer les informations du model caffe pour l'IA, de sectionner les images en acquisition en 3 zones (vue de gauche, vue de droite, vue centrale) et enfin, afficher le résultat des traitement dans une fenêtre graphique.
    
    _note: L'affichage de la fenêtre ne sera utilisée que pour les démos/ présentations du projet. Dans un cas réel, aucun flux ne sera</br> visualisé ni enregistré._
    
        .--------------------------.
        |        |        |        |                     
        |        |        |        |
        |        |        |        |
        |        |        |        |
        |        |        |        |
        |        |        |        |
        |        |        |        |
        .--------------------------.
    _Format des images après sectionnement_
</ul>

### Traffic_Light_Detection</br>
Ici, 2 fonctions sont utilisées pour détecter les feux tricolores de par leurs formes et leurs couleurs:</br>
  - Fonction "find_rect()" => Recherche les formes rectangulaires verticales noires dans un espace colorimétrique HSV. Application de traitement d'image courant:</br>
          > Elévation du contraste pour le noir: cv2.normalize(pixels_noir, 0, 255, cv2.NORM_MINMAX)</br>
          > Construction d'élements structurés de taille 3x3 et de forme rectangulaire: cv2.getStructuringElement()</br>
          > Suppression des faibles contours: cv2.morphologyEx(élements_strcturés, cv2.MORPH_OPEN, kernel)</br>
          > Listing des contours restants: cv2.findContours(img, cv2.RETR_LIST)</br>
          > Pour chaque contours de la liste vérifie ses dimensions: (si w > 100 px et h compris entre w et 2 * w)</br>
          > Recherche de cercles à l'intérieur du rectangle noir trouvé (si 3 cercles alignés, alors le feu est détecté)</br>
  - Fonction "find_circle()" => Recherche les formes circulaires à l'intérieur d'un rectangle noir, vérifie l'alignement verticale des cercle par leur centre, puis analyse la position des couleurs détectées dans ces cercles (si cercle supérieur = rouge ou si cercle inférieur = vert):</br>
          > Changement d'espace colorimétrique BGR2GRay: cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)</br>
          > Lissage gaussien: cv2.GaussianBlur(img, (9, 9))</br>
          > Détection de cercle avec la transformée de Hough: cv2.HoughCircles()</br>
          > Si pour un rectangle, le nombre de cercle détecter à l'intérieur est inférieur à 3, alors je stop.</br>
          > sinon, je récupére leur centre respectif et la taille de leur rayon avec la boucle for</br>
          for (x_centre, y_centre, rayon) in circles:</br>
              sauvegarde(x_centre_i, y_centre_i, rayon_i)</br>
          > Puis avec une condition "if" je test l'alignement des centres sur l'axe des abscisses</br>
          if(x_centre_i and x_centre_i+1) == x_centre_i+2):</br>
              alors condition vérifiée</br>
          > Puis je récupére l'index du cercle avec la valeur en y la plus faible (comme l'axe des y est inversé, la valeur la plus faible nous donne l'index du cercle le plus haut dans l'image). Enfin, je récupère la couleur au centre de ce cercle et si la valeur récupérer pour la composante rouge est supérieur au seuil que j'ai fixé, alors ce cercle est actif et rouge (donc cercle supérieur en</br> rouge c'est bien un feu tricolores).</br>
          > Si, le cercle du haut n'est pas actif, je fais la même opération pour le cercle du bas en testant la couleur verte.</br>
          > Si tout est positif, je dessine les cercles et le rectangle en inscrivant la couleur du feu actif et je renvoi l'information à l'utilisateur, sinon, je ne fais rien car aucune feu n'est détecté.</br>

### Object_Detection</br>
Je me base sur un programme d'intelligence artificiel pré-entrainé.

### Line_Detection</br>
Transformé de hough linéaire

### Color_Detection</br>
Pas utilisé.

## Mis à jour :
&nbsp;&nbsp;&nbsp;- 14/12/2021: Version 1.0.0, Alexandre LEPERS (lepers199)

## Références
https://perso.ensta-paris.fr/~pcarpent/MO102/Cours/Projets/Pr-vision.pdf</br>
https://stackoverflow.com/questions/11386556/converting-an-opencv-bgr-8-bit-image-to-cie-lab</br> https://www.researchgate.net/publication/230601628_Traffic_Lights_Detection_in_Adverse_Conditions_Using_Color_Symmetry_and_Spatiotemporal_Information</br>
https://gist.github.com/bikz05/6fd21c812ef6ebac66e1</br>
https://stackoverflow.com/questions/12187354/get-rgb-value-opencv-python</br>
