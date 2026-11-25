# test.py

from bs4 import BeautifulSoup

# Extraction des informations souhaitées avec Beautiful Soup
with open("index.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

#print(soup)

# Extraction du titre
titre = soup.title.string if soup.title is not None else None
if titre is not None:
    print(f"Titre de la page: {titre}")
else: print("Page sans titre!")

# Extraction des éléments <h1>
h1_texte = soup.find_all('h1')
print(f"Titre - h1: {h1_texte}")

# Extraire tous les éléments <h2>
h2_texte = soup.find_all('h2')
print(f"Produits: {h2_texte}")
print(h2_texte[0])

# Extraire tous les éléments <li>
# Dictionnaire pour stocker les produits
all_products = dict()

# Extraction des noms et des prix des produits dans la liste
products = soup.find_all("li")
for product in products:
    name = product.find("h2").string
    price_str = product.find("p", class_="price").string
    #print(f"## Product: {product} Price: {price_str}")
    # On sépare la chaine avec " " en liste de mots
    price_list = price_str.split(" ")
    #print(f"### {price_list}")
    # On récupère le prix (= deuxième mot)
    all_products[name] = {"prix": price_list[1]}
    
    # Extraction de la description du produit
    # La description est le dernier élément de la liste des paragraphes
    description = product.find_all("p")[-1].string
    all_products[name]["description"] = description

# Affichage des informations extraites
produits = all_products.items()   #Retourne le dict
#for clé, valeur in produits:
#    print(f"- {clé}: {valeur}")
    
