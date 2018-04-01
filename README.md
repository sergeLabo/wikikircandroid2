# wikikircandroid2

Version Android de [WikikIRC](https://wiki.labomedia.org/index.php/WikikIRC)

## Réalisé avec Kivy et Buildozer

Le but de ce projet est de vérifier que buildozer compile bien sur mon PC,
 de se faire plaisir, d'épater la gallerie, de rendre hommage aux bienveillants créateurs de WikikIRC.

### Python 2.7
Sur debian strectch 9.4 dans VirtualBox

Buildozer en python 3.5 ne supporterait pas openssl

### Quelle version de l'interpréteur python ?

[Conseil de la doc Kivy sur Cython](https://kivy.org/docs/installation/installation-linux.html#cython)

Résumé: ça marchera ou pas !

J'ai réussi avec
 sudo pip install Cython==0.23

### Buildozer requirements
requirements = kivy,openssl

La requête pour obtenir les modifications d'une page wikipedia est en https, d'où openssl

La compilation est très longue, beaucoup plus qu'un certain temps.

### IRC
Pas d'import, les fichiers sont dans le dossier.

### Licence

wikikircandroid2 is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

All files are under GNU GENERAL PUBLIC LICENSE Version 3

### Bug connu
#### Bug de kivy
La taille des polices de texte est définie en dpi, mais ça marche mal !

#### Du coup le texte déborde parfois de l'écran

### Merci à
* [La Labomedia](https://labomedia.org/)
* [Le Centre Ressources](https://wiki.labomedia.org/index.php/Accueil)
* [Les Open Ateliers](https://openatelier.labomedia.org/)
* [Le FabLab Atelier du C01N](https://atelierduc01n.labomedia.org/)
