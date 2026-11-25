# Test de fonctions
"""
    Créer un programme qui calcule le salaire horaire d'un employé,
    en fonction de son salaire mensuel et de son nombre d'heures
    travaillées par semaine.
    
    Le programme doit utiliser des fonctions pour effectuer les calculs.
    
    Cf https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/
    7296396-regroupez-des-taches-en-utilisant-des-fonctions
"""

def salaire_mensuel(sal_annuel):
    """
    Cette fonction aclcul le salaire mensuel
    
    Paramètres:
    a(int): salaire annuel
    
    Return:
    int: salaire mensuel
    """
    sal_mensuel = sal_annuel / 12
    return sal_mensuel

def salaire_hebdomadaire(sal_mensuel):
    sal_semaine = sal_mensuel / 4
    sal_semaine = round(sal_semaine, 2)
    return sal_semaine

def salaire_horaire(sal_hebdo, heures_travail):
    sal_horaire = sal_hebdo / heures_travail
    sal_horaire = round(sal_horaire, 2)
    return sal_horaire

salaire_annuel = int(input("Salaire annuel: "))
salaire_hebdoma = float(salaire_hebdomadaire(salaire_mensuel(salaire_annuel)))
print(f"Salaire annuel: {salaire_annuel} CHF.")
print(f"Salaire hebdomadaire: {salaire_hebdoma} CHF.")
heures_semaine_str = (input("Nombre d'heures de travail de la semaine: "))
heures_semaine = int(heures_semaine_str)
salaire_semaine = salaire_horaire(salaire_hebdoma, heures_semaine)
print(f"Salaire horaire: {salaire_semaine} CHF.")