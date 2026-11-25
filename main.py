# Partie 3 - Import packages
"""
    Calculatrice
    https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7296681-importez-des-packages-python
"""
# Import d'un module local
import calculateur.operations
# appel avec nom_dossier.nom_fichier.nom_fonction()

# Varianê:
#from calculateur.operations import multiplication, somme, division, substraction
# Appel uniquement avec le nom de la fonction

if __name__ == '__main__':
    print("Bienvenue sur la mini-calculatrice !")
    print("Test d'utilisation de module(Packages).")
    resultat = calculateur.operations.somme(10, 30)
    print(resultat)
    resultat = calculateur.operations.multiplication(10, 30)
    print(resultat)
    resultat = calculateur.operations.substraction(10, 30)
    print(resultat)
    resultat = calculateur.operations.division(10, 30)
    print(resultat)
