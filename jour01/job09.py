class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        return f"Informations du produit:\nNom : {self.nom}\nPrix HT : {self.prixHT} €\nTVA : {self.TVA}%\nPrix TTC : {self.calculerPrixTTC()} €"

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def obtenirNom(self):
        return self.nom

    def obtenirPrixHT(self):
        return self.prixHT

    def obtenirTVA(self):
        return self.TVA

# Exemple d'utilisation
produit1 = Produit("ordinateur", 1000, 20)
produit2 = Produit("téléphone", 500, 10)
produit3 = Produit("grille-pain", 60, 15)

# Afficher les informations de chaque produit
print(produit1.afficher())
print("\n")
print(produit2.afficher())
print("\n")
print(produit3.afficher())

# Modifier le nom et le prix de chaque produit
produit1.modifierNom("ordinateur reformaté")
produit1.modifierPrixHT(900)

produit2.modifierNom("téléphone reformaté")
produit2.modifierPrixHT(600)

produit3.modifierNom("brûle-pain")
produit3.modifierPrixHT(50)


# Afficher les nouveaux nom et prix des produits
print("\nNouveaux prix des produits :")
print(" ")
print("Nouveau prix de l'", produit1.obtenirNom(), ":", produit1.obtenirPrixHT(), "€")
print("Nouveau prix du", produit2.obtenirNom(), ":", produit2.obtenirPrixHT(), "€")
print("Nouveau prix du", produit3.obtenirNom(), ":", produit3.obtenirPrixHT(), "€")
