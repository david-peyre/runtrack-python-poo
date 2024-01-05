class Personnage:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1

    def position(self):
        return self.x, self.y


# Exemple d'utilisation
personnage1 = Personnage()

# Affichage de la position initiale
print("Position initiale :", personnage1.position())

# Déplacer le personnage
personnage1.droite()
personnage1.haut()
personnage1.gauche()
personnage1.gauche()
personnage1.gauche()

# Affichage de la nouvelle position
print("Nouvelle position :", personnage1.position())
