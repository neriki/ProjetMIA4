Boniface Eric MIA4

#Projet : explorateur de configuration Unix à distance

##Présentation

L’explorateur de configuration Unix à distance permet d’explorer le contenu d’un ordinateur Unix à partir de n’importe quel ordinateur relié par un réseau TCP/IP au serveur. Il se compose de deux parties, un logiciel serveur tournant sur le serveur Unix et un logiciel client tournant sur le poste client. Le logiciel client étant écrit en Python, il peut fonctionner sur n’importe quel ordinateur faisant tourner l’interpréteur Python (PC sous Microsoft Windows, Pc sous Linux, station de travail sous Unix, Ordinateur Apple Macintosh).

##Le serveur 

Le serveur est écrit en Python Il s’exécute sur le serveur Unix. Il attend une connexion sur le port 1236. Il ne supporte qu’une connexion à la fois. La connexion entre le serveur le client se fait à partir de commande, le serveur attend une commande du client, celui ci lui envoie, le serveur lui répond en lui renvoyant une chaîne de caractères. Les commandes du clients sont des chaînes de caractères. La réponse du serveur au client se compose d’une chaîne de caractères terminées par la chaîne «***FINENVOI*** ». La commande cliente « fin » ferme la connexion et le serveur se met en attente d’une nouvelle connexion.

##Le client

Le client est écrit en Python, il utilise la bibliothèque graphique Tkinter. Cette bibliothèque permet d’afficher des fenêtres en mode graphique. L’interface se compose de quatre grande partie :
La liste des boutons qui permettes d’envoyer des commandes au serveur .
La barre de texte affichant le répertoire courant sur le serveur Unix.
La barre de saisie des répertoire et des noms de fichiers.
La fenêtre de texte ou sont affiché le contenu des fichiers et ou est listé le répertoire courant sous Unix.
 

Quand on lance l’application, la première fenêtre n’affiche rien de spécial. On commence par saisir l’adresse IP du serveur auquel on veut se connecter dans la barre de saisie, puis on clique sur le bouton connexion .
![1er ecran](https://raw.githubusercontent.com/neriki/ProjetMIA4/master/1ecran.jpg)
Une fois connecter au serveur, le contenu du répertoire courant est affiché dans la zone de texte.
![connect](https://raw.githubusercontent.com/neriki/ProjetMIA4/master/connect.jpg)
Le bouton « Dir » Permet de lister le répertoire courant. 
Le bouton « Version » indique quelle est la version d’Unix utilisé par le serveur ainsi que le type de machine. 
Le bouton « Ouvrir fichier » ouvre le fichier dont le nom à été saisie dans la barre de saisie.
![voir fichier](https://raw.githubusercontent.com/neriki/ProjetMIA4/master/voirfich.jpg) 
Le bouton « Aide » affiche l’aide.
Le bouton « cd .. » descend d’un niveau de répertoire.
Le bouton « cd » va dans le répertoire dont le nom à été saisie dans la barre de saisie.

