# Exemple de dictionnaire imbriqué
etudiant = {
    "nom": "Alexandre",
    "cours": {
        "mathématiques": 85,
        "physique": 90,
        "informatique": 95
    }
}

# Accès aux éléments imbriqués
cours_info = etudiant.get("cours", "Non spécifié!")
print(cours_info)

note_etudiant = etudiant.get("cours", {}).get("physique", "None")
print(note_etudiant)

# Lecture des clés
print("Liste des clés:")
for clefs in etudiant:
    print(clefs)
print(type(clefs))

print("Liste des valeurs")
for valeurs in etudiant.values():
    print(valeurs)
print(type(valeurs))

print("Liste des items")
for items in etudiant.items():
    print(items)
print(type(items))
