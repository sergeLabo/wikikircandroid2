# wikikircandroid2

Version Android de [WikikIRC](https://wiki.labomedia.org/index.php/WikikIRC)

## Réalisé avec Kivy et Buildozer

### Python 2.7
Sur debian strectch 9.4 dans VirtualBox

Buildozer en python 3.5 ne supporterais pas openssl

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

### Bug connu
La taille des polices de texte est définie en dpi, mais ça marche mal !
