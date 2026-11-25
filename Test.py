# Apprendre la programmation avec python - page 23
# 3.1 - 13.11.26
# Bloc de code
def exemple():
    print("Je suis indenté")
    limite = 12
	# Sélection d'une partie du texte
    for i in range(limite):
        print(f"Texte quelconque lu par range(limite). Passage: {i}")

# 2ème bloc
def autre():
    print ("Texte indenté dans une autre fonction!")

# Fonctions du chapitre 8

# 1ere fonction
def bonjour(prenom, nom):
    print(f"Bonjour {prenom} {nom}")

# Fonction chapitre 8.3 
def envoi_mail(mail_emetteur, mail_destinataire, sujet, message):
    print(f"De: {mail_emetteur}")
    print(f"To: {mail_destinataire}")
    print(f"Subjet: {sujet}")
    print(message)
    return(True)

# Fonctions chapitre 9.11
def ajout_carnet(carnet, nom, email, telephone):
    carnet[nom] = {"email": email, "Téléphone": telephone}

def supprimer_personne(carnet, nom):
    if nom in carnet:
        del carnet[nom]
    else:
        print("Personne non trouvée!")

def afficher_carnet(carnet):
    for nom, infos in carnet.items():
        print(f"{nom}: {infos}")

def rechercher_personne(carnet, nom):
    if nom in carnet:
        print(f"{nom}: {carnet[nom]}")
    else:
        print("Personne non trouvée")

# appel des fonctions:
#exemple()
#autre()
# Pour masquer les lignes: Sélection des lignes puis Shift+Ctrl+[
# Pour remontrer les lignes: Shift+Ctrl+]
# Page 40 - opérateurs
#x = 25
#y = 7#

## Division
#division = x / y
#print(f"Résultat de la division de  x par y: {division}")#

## Division entière
#division_entiere = x // y
#print(f"Résultat de double barre: {division_entiere}")
#	
## Modulo
#modulo = x % y 
#print(f"x mod y: {modulo}")#

## Exponentielle
#puissance = x ** y 
#print(f"x puissance y: {puissance}")

# page 45 - Chapitre 6

# # Boucle for
# pour x itérations
# x = 12
# for i in range(x):
#     print(f"Boucle parcourues x fois. N° de l'itération: {i}")# 

# # Boucle while
# cible = 12
# nombre = 2
# while nombre < cible:
#     nombre += 1
#     print(f"nombre est égal à {nombre}")
# print(f"Fin de boucle, nombre vaut {nombre}")

# # Boucles imbriquées
# import time    # Pour temporiser
# for ligne in range (10):
#     print(f"Ligne n°: {ligne}", end = " ")
#     for colonne in range (10):
#         time.sleep(0.1)
#         print(ligne, end = (" "))  # Pas de retour à la ligne
#     print(" ")

# 6.3 - Page 53
# range (fin)
# range (debut, fin)
# range (debut, fin, incrément)

# # Affiche les 100 premiers éléments
# debut = 20
# limite = 30
# increment = 1
# for i in range(debut, limite + 1, increment):
#     print(f"Elément {i}")# 

# i = 1
# while i <= limite - debut:
#     print(f"Elément {i}")
#     i += increment 

# Chapitre 7 - page 60 - Nombre caché
# if - else & try - except
# print("Quel est le nombre caché ?")
# nombre_cache = 67
# while True: # boucle infinie! Il faudra en sortir avec un break.
#     try:
#         essai = int(input("Quel est le nombre ?"))
#     except ValueError: 
#         print("Veuillez entrez un nombre entier compris entre 1 et 100, SVP!")
#         continue    # Retour au début de la boucle# 

#     if essai == nombre_cache:
#         print(f"Bravo, vous avez trouvé le nombre caché: {essai}")
#         break   # Fin de boucle# 

#     else:
#         if essai < nombre_cache:
#             print("Le nombre caché est plus grand")
#             continue
#         else:
#             print("Le nombre caché est plus petit")
#             continue

# Chapitre 8 - Fonctions
# prenom = input("Quel ton prénom: ")
# nom = input("et ton nom ? ")
# bonjour(prenom, nom)

# # Manipuler les string
# chaine = " Bonjour,  comment  ça  va  ?"
# longueur = len ( chaine ) # 30
# chaine_en_minuscules = chaine.lower()
# chaine_en_majuscules = chaine.upper()
# chaine_sans_espaces = chaine.strip()
# chaine_remplacee = chaine.replace("Bonjour", "Salut")
# liste_de_mots = chaine.split(" ")
# print ( " Chaine de base: " , chaine )
# print ( " Longueur de la chaine: " , longueur)
# print ( " En minuscule: " , chaine_en_minuscules)
# print ( " En majuscule: " , chaine_en_majuscules)
# print ( " Sans espace: " , chaine_sans_espaces)
# print ( " Remplacee: " , chaine_remplacee)
# print ( " Une liste: " , liste_de_mots)

# # 8.3 - Envoi mail
# emetteur = input("Adresse mail de l'émetteur: ")
# destinataire = input("Adresse mail du destinataire: ")
# sujet = input("Sujet du mail: ")
# message = input("Texte du mail: ")# 

# print("Envoi du message")
# envoi = envoi_mail(emetteur, destinataire, sujet, message)
# if envoi:
#     print("Message envoyé")
# else: print("Problème d'envoi")

# Chapitre 9 - Listes, ...
# liste_composants = [ " CPU " , " GPU " , " carte mere " , "alimentation" , " ventirad " , " cables " ]
# liste_courses = [ " carottes " , " pommes " , " orange " ]
# liste_quelconque = [1 ,2 ,5 , 8.3 , 7.2 , 1254.054 , 4728/17, " penser a regarder les etoiles " ]
# liste_de_liste = [ liste_composants , liste_courses ,liste_quelconque ]
# print ( liste_de_liste )
# print ( liste_courses[0])
# print ( liste_courses[2])# 

# # Ajouter des elements a la liste
# liste_courses.append("poire")
# liste_courses.append("banane")
# liste_courses.append("cerise")
# # Afficher la liste# 

# print(liste_courses)
# print ( liste_courses[5])# 

# # Ajouter plusieurs elements a la liste: on ajoute une liste
# liste_courses.extend(["kiwi" , " kaki " , " fraise "])
# print(liste_de_liste)# 

# # for element in liste_de_liste:
# #     print(element)# 

# # Avec enumerate
# # pour acceder à l’indice de l’élément:
# for indice, fruit in enumerate(liste_courses):
#     print(f"Indice dans la liste_courses: {indice}, Compostant de la liste_courses: {fruit}")

# # 9.2 - Chaines de carctères
# chaine_test = "Voici une ligne texte mémorisée dans la variable chaine_test!"
# #for indice, cc in enumerate(chaine_test):
# #    print(f"Position: {indice} , Caractère: {cc}")
# print(chaine_test[0], chaine_test[3], chaine_test[12])

# 9.4 - Projet

# 9.4.1 - Exercice 1 : Créer et afficher une liste
# 1. Créez une liste appelée outils contenant les éléments suivants : "marteau",
# "tournevis", "clé".
# 2. Affichez cette liste.

# 9.4.2 - Exercice 2 : Ajouter des éléments à une liste
# 1. Ajoutez "scie" à la liste outils en utilisant la méthode append.
# 2. Ajoutez "pince" et "lime" à la liste outils en une seule opération avec
# la méthode extend.
# 3. Affichez la liste mise à jour.

# 9.4.3 - Exercice 3 : Accéder aux éléments d’une liste
# 1. Affichez le premier élément de la liste outils.
# 2. Affichez le troisième élément de la liste outils.
# 3. Affichez le dernier élément de la liste outils.

# # 9.4.1
# outils = ["Marteau", "Tournevis", "Clé"]
# print(f"Liste d'outils: {outils}")
# # 9.4.2
# outils.append("Scie")
# outils.extend(["Pince", "Lime"])
# print(f"Liste modifiée: {outils}")
# # 9.4.3 
# print(f"1er élément de la liste Outils: {outils[0]}")
# print(f"3ème élément: {outils[2]}")
# print(f"Dernier élément: {outils[-1]}")
# # 9.4.4 - Supprimer des éléments
# outils.remove("Tournevis")
# element_supprime = outils.pop()
# print(f"Dernier élément supprimé: {element_supprime}")
# print(f"Liste modifiée: {outils}")
# # 9.4.5 - Itérer
# legumes = ["carotte", "pomme de terre", "poivron"]
# i = 1
# for item in legumes:
#     print(f"Elément {i} de la liste: {item}")
#     i += 1

# # 9.4.6 - Listes imbriquées
# liste_course = [outils, legumes] # C'est comme une matrice de strings à 2 dimensions
# print(f"Liste d'achats: {liste_course}")
# print(f"2ème élément de la 2ème liste: {liste_course[1][1]}")# # 9.4.7 - Ajouter un élément aux listes imbriquées

# # 9.4.7
# legumes.append("Brocoli") 
# print(f"Liste d'achats mmodifiée ? : {liste_course}")

# # 9.4.8 - Conditions sur une liste
# liste_nombres = [1]
# for i in range(1, 10):
#     liste_nombres.append(i + 1)
#     print(f"Liste de nombres: {liste_nombres}")
# for i in range(1, 10):
#     nombre = (i % 2)
#     if nombre == 0:
#         print(f"Nombre pair: {i}")
#     else:
#         print(f"Nombre impair: {i}")

# # 9.4.9 - Slicing: appel de caractères spécifiques
# liste_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# print(liste_alphabet)
# print(f"Eléments 0 à 2: {liste_alphabet[0]} , {liste_alphabet[1]}, {liste_alphabet[2]}")
# print(f"3 derniers éléments: {liste_alphabet[-3]} , {liste_alphabet[-2]}, {liste_alphabet[-1]}")
# print(f"Eléments d'indice 3 à 6: {liste_alphabet[3]} , {liste_alphabet[4]}, {liste_alphabet[5]}, {liste_alphabet[6]}")

# 9.6 - Tuples 22.11.26
# Problèmes avec les exemples de code!

# 9.7 - Set 22.11.26
# # Un set ne peut pas contenir 2x la même valeur!
# # On peut donc éliminer les doublons avec un set.
# liste_1 = [1, 5, 45, 4, 5, 1, 54, 2, 3, 54]
# liste_2 = [12, 3, 17, 14, 15, 11, 55, 21, 23, 54]
# set_1 = {1, 5, 475, 4}
# set_2 = set(["a", "b", "c", "d",]) 
# print(set_1)
# print(set_2)
# set_1.add(45)
# print(set_1)
# set_1.remove(5)
# print(set_1)
# set_unis = set_1.union(set_2)
# print(set_unis)
# liste_3 = liste_1 + liste_2
# print(liste_3)
# set_4 = set(liste_3)
# print(set_4)
# print(type(set_4))

# 9.8 - Dictionnaires 22.11.26
# dico_membre = {
#     "Nom": "Romay", 
#     "Prenon": "Pat", 
#     "Mail": "pat.romailler@gmail.com", 
#     "Type de membre": "Couple", 
#     "Adresse": "Ch. de Pécheret", 
#     "N°": 14, 
#     "N° postal": 1424, 
#     "Lieu": "Champagne" }
# print(dico_membre.values())
# print(dico_membre.get("Mail"))
# print(dico_membre.get("Type de membre"))
# dico_membre["Date de naissance"] = "18.07.1954"
# print(dico_membre)
# dico_membre["Date de naissance"] = "10.06.2010"
# print(dico_membre)
# # Itérer un dico
# for cle, valeur in dico_membre.items():
#     print(f"La clef {cle} vaut: {valeur}")# 

# # 9.10 - Carnet d'adresse
# carnet = {}
# ajout_carnet(carnet, "Pat", "pat@romailler.ch", "076 512 00 78")
# print(carnet)
# ajout_carnet(carnet, "Jo", "jo@romailler.ch", "079 650 97 35")
# ajout_carnet(carnet, "Kim", "kim@romailler.ch", "078 125 67 89")
# ajout_carnet(carnet, "Yolan", "yolan@romailler.ch", "076 425 77 51")# 

# afficher_carnet(carnet)
# rechercher_personne(carnet, 'Jo')
# supprimer_personne(carnet, "Yolan")
# afficher_carnet(carnet)

# 9.11 - Liste de dict
utilisateurs =[{"Nom": "Alice", "email": "alice@gmail.com", "jeu_prefere": "Trio"},
{"Nom": "Bob", "email": "bob@gmail.com", "jeu_prefere": "Uno"},
{"Nom": "Claude", "email": "claude@gmail.com", "jeu_prefere": "The game"}]
for membre in utilisateurs:
    print(f"Nom: {membre['Nom']}, email: {membre['email']}, Jeu préféré: {membre['jeu_prefere']}")