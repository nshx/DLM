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
Pour lancer l'application, on lance la commande : "node ." une fois à la racine du projet</br>
Au lancement de la commande, on se connecte au broker mqtt local. Ensuite on reçoit et traite les messages mqtt afin de déclencher un affichage.</br>

## Updates :
&nbsp;&nbsp;&nbsp;- 14/12/2021: Version 1.0.0, Arthur BORG
