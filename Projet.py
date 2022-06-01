#!/usr/bin/python

from hashlib import sha256

import os 

print  ("--------------- Crypter un fichier avec sha 256 ---------------" )

choix = input("voulez vous crypter ou décripter un fichier c-> crypté , d-> decrypté :")
 
if choix == "c":

	entree = input("entrez le nom du fichier a chifrer/dechifrer :")
	if os.path.exists(entree): 
		avis = input ( " y -> pour canger le contenue du fichier , n -> pour chifrer le fichier sans changement :")
		if avis == "y" : 
			contenue = input ("ecrire le comptenue du fichier :  ")
			fichier = open (entree,'w')
			fichier.write(contenue )
			fichier.close()
		elif avis == "n" : 
			print ("Le contenue du fichier ne change pas : ")
			with open (entree ,'r') as f :
				for ligne in  f :
					print (ligne)
			f.close()
		else : 
			print  ("Erreur")

		sortie =input("entrez le nom du fichoier final (crypter) :") 
		key = input ("Donnez la clé : ")
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
	entree = input("entrez le nom du fichier dechifrer :")
	if os.path.exists(entree): 
	
		sortie =input("entrez le nom du fichoier final (décrypter) :") 
		key = input ("Donnez la clé (La clé dois etre la meme que celle du décriptage) : ")
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