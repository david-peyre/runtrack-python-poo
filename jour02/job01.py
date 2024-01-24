class Rectangle:

    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur

    # Accesseurs
    def getLongueur(self):
        return self._longueur

    def getLargeur(self):
        return self._largeur

    # Mutateurs
    def setLongueur(self, nouvelle_longueur):
        self._longueur = nouvelle_longueur

    def setLargeur(self, nouvelle_largeur):
        self._largeur = nouvelle_largeur

# Exemple d'utilisation
rectangle1 = Rectangle(10, 5)

# Afficher les valeurs initiales
print("Longueur initiale :", rectangle1.getLongueur())
print("Largeur initiale :", rectangle1.getLargeur())

# Changer les valeurs
rectangle1.setLongueur(15)
rectangle1.setLargeur(8)

# Afficher les nouvelles valeurs
print("\nNouvelle longueur :", rectangle1.getLongueur())
print("Nouvelle largeur :", rectangle1.getLargeur())
