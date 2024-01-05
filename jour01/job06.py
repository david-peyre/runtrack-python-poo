class Animal:

    def __init__(self):
        self.age = 0
        self.prenom = ""

    def afficher_age(self):
        print("L'âge de l'animal :", self.age, "ans")

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom
        print("L'animal se nomme", self.prenom)
 

# Instanciation d'un objet Animal
animal1 = Animal()

# Affichage de l'âge initial
animal1.afficher_age()

# Faire vieillir l'animal
animal1.vieillir()

# Affichage de l'âge après vieillissement
animal1.afficher_age()

# Nommer l'animal et afficher son nom en console
animal1.nommer("Luna")
