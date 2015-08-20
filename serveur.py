#Eric Boniface MIA4
#Serveur
import socket
import os
import string

#Creation du socket de communication
serversocket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 1236))
serversocket.listen(5)

#Fonction d'envoie des paquets
def envoyer(chaine_s,socket_s):
	socket_s.send(chaine_s)
	socket_s.send("***FINENVOI***")

def fversion():
	version=os.uname()
	message=version[1]+"\nSous "
	message=message+version[0]+" "
	message=message+version[2]+" compiled "
	message=message+version[3]+"\nProcesseur:"
	message=message+version[4]
	return message

#fonction qui liste le contenu d'un repertoire
def fdir():
	message=""
	for element in os.listdir(os.getcwd()):
		if message=="":
			message=element
		else:	
			message=message + " \n" + element
	return message

#fonction qui extrait le contenu d'un fichier
def fouvrir(fichier):
	message=""
	fdesc=open(fichier, 'r')
	sortie=fdesc.readline()
	while sortie != "" :
		message=message + sortie 
		sortie=fdesc.readline()
	fdesc.close()
	return message

#fonction qui envoie le nom du repertoire courant
def frepcour():
	return os.getcwd()
	
#fonction qui change de repertoire
def fcd(rep):
	message="Changement de rep."
	os.chdir(rep)
	return message

#fonction qui envoie l'aide
def faide():
	message="Commande sans argument:\n"
	for caide in commandes0arg:
		message=message+caide[0]+" : "+caide[1]+"\n"
	message=message+"fin : Deconnexion\n"
	message=message+"\nCommande avec un argument:\n"
	for caide in commandes1arg:
		message=message+caide[0]+" : "+caide[1]+"\n"
	return message

#Tableau des fonctions
commandes0arg=[["repcour","Affiche le repertoire courant",frepcour],
	["dir","Affiche la liste des fichiers dans le repertoire courant",fdir],
	["version","Affiche des informations sur l'OS",fversion],
	["aide","Affiche cette aide",faide]]

commandes1arg=[["cd","Change le repertoire courant",fcd],
	["ouvrir","Affiche le contenu d'un fichier",fouvrir]]

#Boucle infine de gestion des evenements
while 1:
	#attente de connexion d'un client
	(clientsocket, address) = serversocket.accept()
	#des qu'un client est connecte on affiche son adresse IP
	print address
	while 1:
		#attente des commandes envoye par le client
		retour=clientsocket.recv(20)
		print retour
		lcommande=string.split(retour)
		message="Commande inconnue!"

		if retour=="fin":
			#Si c'est la commande de fin on arrete la connection
			clientsocket.close()
			message="Deconnexion"
			break
		#Recherche dans les tableaux de fonctions la fonctions 
		#correspondantes a la commande envoyees et execution 
		#de cette fonction
		for comm in commandes0arg:
			if lcommande[0]==comm[0]:
				message=comm[2]()
		for comm in commandes1arg:
			if lcommande[0]==comm[0]:
				message=comm[2](lcommande[1])

		#on envoie au client le resultat de la commande 
		#execute
		envoyer(message,clientsocket)
