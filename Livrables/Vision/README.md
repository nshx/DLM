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
src: Algorithme de détection de feux tricolores terminé ainsi que celui pour la détection d'objet.</br>

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
Dans une invite de commande, déplaceé-vous jusqu'à l'emplacement des codes sources python.</br>
### WINDOWS:
  > python Single_Video_Flux.py</br>
ou</br>
  > python Multiple_Video_Flux.py</br>
### LINUX:
 > ./Single_Video_Flux.py</br>
ou</br>
  > ./Multiple_Video_Flux.py</br>

### Fonctionnement des différents algorithmes 
#### Single_Flux_Video & Multiple_Flux_Video.</br>

#### Traffic_Light_Detection</br>

#### Object_Detection</br>

#### Line_Detection</br>

#### Color_Detection</br>


## Updates :
&nbsp;&nbsp;&nbsp;- 14/12/2021: Version 1.0.0, Alexandre LEPERS (lepers199)

## References
https://perso.ensta-paris.fr/~pcarpent/MO102/Cours/Projets/Pr-vision.pdf</br>
https://stackoverflow.com/questions/11386556/converting-an-opencv-bgr-8-bit-image-to-cie-lab</br> https://www.researchgate.net/publication/230601628_Traffic_Lights_Detection_in_Adverse_Conditions_Using_Color_Symmetry_and_Spatiotemporal_Information</br>
https://gist.github.com/bikz05/6fd21c812ef6ebac66e1</br>
https://stackoverflow.com/questions/12187354/get-rgb-value-opencv-python</br>
