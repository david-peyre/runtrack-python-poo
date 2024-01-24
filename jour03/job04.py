class Joueur:

    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquer_un_but(self):
        self.buts_marques += 1
        print(f"{self.nom} a marqué un but !")

    def effectuer_une_passe_decisive(self):
        self.passes_decisives += 1
        print(f"{self.nom} a effectué une passe décisive !")

    def recevoir_un_carton_jaune(self):
        self.cartons_jaunes += 1
        print(f"{self.nom} a reçu un carton jaune !")

    def recevoir_un_carton_rouge(self):
        self.cartons_rouges += 1
        print(f"{self.nom} a reçu un carton rouge !")

    def afficher_statistiques(self):
        print(f"Statistiques de {self.nom} (#{self.numero}, {self.position}) :")
        print(f"Buts marqués : {self.buts_marques}")
        print(f"Passes décisives : {self.passes_decisives}")
        print(f"Cartons jaunes : {self.cartons_jaunes}")
        print(f"Cartons rouges : {self.cartons_rouges}")
        print()


class Equipe:

    def __init__(self, nom):
        self.nom = nom
        self.liste_joueurs = []

    def ajouter_joueur(self, joueur):
        self.liste_joueurs.append(joueur)
        print(f"Le joueur {joueur.nom} a été ajouté à l'équipe {self.nom}")

    def afficher_statistiques_joueurs(self):
        print(f"Statistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.liste_joueurs:
            joueur.afficher_statistiques()

    def mettre_a_jour_statistiques_joueur(self, nom_joueur, action):
        for joueur in self.liste_joueurs:
            if joueur.nom == nom_joueur:
                if action == "but":
                    joueur.marquer_un_but()
                elif action == "passe_decisive":
                    joueur.effectuer_une_passe_decisive()
                elif action == "carton_jaune":
                    joueur.recevoir_un_carton_jaune()
                elif action == "carton_rouge":
                    joueur.recevoir_un_carton_rouge()
                else:
                    print("Action non reconnue.")
                break


# Créer plusieurs joueurs
joueur1 = Joueur("Messi", 10, "Attaquant")
joueur2 = Joueur("Ronaldo", 7, "Attaquant")
joueur3 = Joueur("Neymar", 11, "Attaquant")
joueur4 = Joueur("Modric", 8, "Milieu")

# Créer deux équipes
equipe1 = Equipe("Barcelone")
equipe2 = Equipe("Real Madrid")

# Ajouter les joueurs aux équipes
equipe1.ajouter_joueur(joueur1)
equipe1.ajouter_joueur(joueur3)
equipe2.ajouter_joueur(joueur2)
equipe2.ajouter_joueur(joueur4)

# Afficher les statistiques initiales des joueurs
equipe1.afficher_statistiques_joueurs()
equipe2.afficher_statistiques_joueurs()

# Simuler un match
equipe1.mettre_a_jour_statistiques_joueur("Messi", "but")
equipe2.mettre_a_jour_statistiques_joueur("Ronaldo", "passe_decisive")
equipe1.mettre_a_jour_statistiques_joueur("Neymar", "carton_jaune")
equipe2.mettre_a_jour_statistiques_joueur("Modric", "carton_rouge")

# Afficher les statistiques après le match
equipe1.afficher_statistiques_joueurs()
equipe2.afficher_statistiques_joueurs()
