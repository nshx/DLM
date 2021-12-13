## DESCRIPTION
### Application Serveur web embarqué permettant l'affichage de données.</br>
Cette application permet au conducteur de connaître les éléments détecter par les caméras avant et/ou arrière.</br>
L'application lance un serveur web local et permet de voir le dernier élément détecter.</br>

</ul>

## Livrable
Dans le dossier, vous trouverez un script java qui fait la connexion mqtt avec notre broker local, un dossier public incluant les images et différentes pages web les fichiers packages nécessaires au lancement du serveur web via express et le dossier zippé node-modules.</br>

## Installation
Télécharger tout le dossier.</br>
Dezipper le dossier node-modules et laisser dossier dezippé à la racine</br>
Via lignes de commandes, installer la dernière version de nodejs.</br>
Si vous rencontré des problèmes avec les versions, vous pouvez vous référer à ce site :
https://joshtronic.com/2018/05/08/how-to-install-nodejs-10-on-ubuntu-1804-lts/</br>

### Fonctionnement de l'application
Au lancement de l'application, on appuie sur le bouton scan pour lancer l'acquisition.</br>
Le bouton check permet de vérifier que les modules que nous cherchons ont bien été détecté par l'application. </br>
Si ce n'est pas le cas, on relance une acquisition.</br>

Une fois les trois modules trouvés on envoie en commande curl des requètes permettant de mettre à jour la base de données utilisé par l'application Web et l'API.</br>
L'application Web prend alors le relai pour géolocaliser l'utilisateur.</br>

## Updates :
&nbsp;&nbsp;&nbsp;- 13/12/2021: Version 1.0.0, Arthur BORG
