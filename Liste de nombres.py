# Saisie de la liste de nombres
nombres_str = input("Saisir une suite de nombres séparés par  ,: ")

# Supprimer les ,
liste_nombres_str = nombres_str.split(",")
print(liste_nombres_str)

# nb de string dans la liste
nb_nombres = len(liste_nombres_str)   
print(f"Nombre d'éléments: {nb_nombres}")

# Transformation des strings en nombres entiers
liste_nb_entier = []
for nombres_str in liste_nombres_str:
    nombre_entier = int(nombres_str)
    liste_nb_entier.append(nombre_entier)
print(liste_nb_entier)
                 
# Calcul de la somme des nombres                 
somme = 0
for nombre in liste_nb_entier:
    somme += nombre
print(f"Somme des nombres = {somme}")

# Calcul de la moyenne
moyenne = somme / nb_nombres
print(f"Moyenne des nombres: {moyenne}")

# Recherche des nombres supérieurs à la moyenne
nb_nombres_sup = 0
print("Nombres supérieurs à la moyenne: ")
for i in range(nb_nombres):
    if liste_nb_entier[i] > moyenne:
        nb_nombres_sup += 1
        print(liste_nb_entier[i])
print(f"Il y a {nb_nombres_sup} nombres supérieurs à la moyenne.")
    



