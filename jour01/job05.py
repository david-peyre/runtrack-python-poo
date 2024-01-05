class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print("Coordonnées du point : ({}, {})".format(self.x, self.y))

    def afficherX(self):
        print("La coordonnée x est :", self.x)

    def afficherY(self):
        print("La coordonnée y est :", self.y)

    def changerX(self, nouvelle_valeur_x):
        self.x = nouvelle_valeur_x

    def changerY(self, nouvelle_valeur_y):
        self.y = nouvelle_valeur_y

        
# Exemple d'utilisation de la classe Point
point1 = Point(2, 5)

# Affichage des coordonnées initiales
point1.afficherLesPoints()

# Affichage de la coordonnée x
point1.afficherX()

# Affichage de la coordonnée y
point1.afficherY()

# Changement des coordonnées
point1.changerX(10)
point1.changerY(7)

# Affichage des nouvelles coordonnées
point1.afficherLesPoints()
