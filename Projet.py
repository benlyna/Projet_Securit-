#!/usr/bin/python

from hashlib import sha256

import os 

print  ("--------------- Crypter un fichier avec sha 256 ---------------" )

choix = input("Voulez vous crypter ou décripter un fichier c-> crypté , d-> decrypté :")
 
if choix == "c":

	entree = input("Entrez le nom du fichier a chiffrer :")
	if os.path.exists(entree): 
		avis = input ( " y-> pour changer le contenue du fichier , n-> pour chiffrer le fichier sans changement :")
		if avis == "y" : 
			contenu = input ("Ecrire le contenu du fichier :  ")
			fichier = open (entree,'w')
			fichier.write(contenu )
			fichier.close()
		elif avis == "n" : 
			print ("Le contenu du fichier ne change pas : ")
			with open (entree ,'r') as f :
				for ligne in  f :
					print (ligne)
			f.close()
		else : 
			print  ("Erreur")

		sortie =input("Entrez le nom du fichier final (crypté) :") 
		key = input ("Donnez la clé de chiffrement : ")
		keys = sha256(key.encode('utf-8')).digest()

		with open(entree,'rb') as f_entree:
			with open (sortie,'wb+') as f_sortie : 
				i=0
				while f_entree.peek():
					c = ord(f_entree.read(1))
					j = i % len(keys)
					b = bytes([c^keys[j]])
					f_sortie.write(b)
					i = i + 1
	
	else : 
		print  ("Ce fichier n'existe pas! ")
			
elif choix == "d":
	entree = input("Entrez le nom du fichier chiffré :")
	if os.path.exists(entree): 
	
		sortie =input("entrez le nom du fichier final (décrypté) :") 
		key = input ("Donnez la clé de déchiffrement (La clé doit etre la meme que celle du décriptage) : ")
		keys = sha256(key.encode('utf-8')).digest()
	
		with open(entree,'rb') as f_entree:
			with open (sortie,'wb+') as f_sortie : 
				i=0
				while f_entree.peek():
					c = ord(f_entree.read(1))
					j = i % len(keys)
					b = bytes([c^keys[j]])
					f_sortie.write(b)
					i = i + 1
	
		with open (sortie ,'r') as f :
				for ligne in  f :
					print (ligne)
		f.close()
	
	else:
		print  ("Ce fichier n'existe pas! ")
else : 
		print  ("Erreur")
