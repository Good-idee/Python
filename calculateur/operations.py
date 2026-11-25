# Open CR - Partie 3 - Import packages
"""
    Calculatrice - module operations
    https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7296681-importez-des-packages-python
"""
 
def somme(a, b):
    valeur_retour = a + b
    return valeur_retour

def substraction(a, b):
    valeur_retour = a - b
    return valeur_retour

def multiplication(a, b):
    valeur_retour = a * b
    return valeur_retour

def division(a, b):
    valeur_retour = 0
    if b != 0:
        valeur_retour = a / b
    else:
        print("Erreur : division par zéro !")
    return valeur_retour

