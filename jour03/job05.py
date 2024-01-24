import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        # La méthode attaquer génère des dégâts aléatoires entre 5 et 15
        degats = random.randint(5, 15)
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")
        adversaire.vie -= degats  # Les dégâts sont soustraits à la vie de l'adversaire

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisir_niveau(self):
        # Le joueur choisit le niveau de difficulté (1, 2 ou 3)
        self.niveau = int(input("Choisissez le niveau de difficulté (1, 2 ou 3) : "))

    def lancer_jeu(self):
        self.choisir_niveau()

        # Les points de vie du joueur et de l'ennemi dépendent du niveau de difficulté
        points_de_vie_joueur = self.niveau * 10
        points_de_vie_ennemi = self.niveau * 5

        # Création des instances de la classe Personnage pour le joueur et l'ennemi
        joueur = Personnage("Joueur", points_de_vie_joueur)
        ennemi = Personnage("Ennemi", points_de_vie_ennemi)

        # Boucle de combat : le combat se déroule jusqu'à ce que la vie d'un des personnages atteigne 0
        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)  # Le joueur attaque l'ennemi
            if ennemi.vie <= 0:
                print(f"{ennemi.nom} a été vaincu ! {joueur.nom} remporte la partie.")
                break

            ennemi.attaquer(joueur)  # L'ennemi attaque le joueur
            if joueur.vie <= 0:
                print(f"{joueur.nom} a été vaincu ! {ennemi.nom} remporte la partie.")
                break

            # Affichage des points de vie après chaque tour de combat
            print(f"{joueur.nom} - Points de vie : {joueur.vie}")
            print(f"{ennemi.nom} - Points de vie : {ennemi.vie}")

# Utilisation du jeu
jeu = Jeu()
jeu.lancer_jeu()
