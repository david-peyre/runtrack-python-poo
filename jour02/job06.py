class Commande:
    def __init__(self, numero_commande):
        self._numero_commande = numero_commande
        self._plats_commandes = {}
        self._statut_commande = "En cours"

    # Méthode privée pour calculer le total de la commande
    def _calculer_total(self):
        total = sum(plat["prix"] for plat in self._plats_commandes.values())
        return total

    # Méthode pour ajouter un plat à la commande
    def ajouter_plat(self, nom_plat, prix_plat):
        self._plats_commandes[nom_plat] = {"prix": prix_plat, "statut": self._statut_commande}
        print(f"Plat {nom_plat} ajouté à la commande.")

    # Méthode pour annuler une commande
    def annuler_commande(self):
        self._statut_commande = "Annulée"
        print("Commande annulée.")

    # Méthode pour afficher la commande avec son total à payer
    def afficher_commande(self):
        total = self._calculer_total()
        print(f"Commande #{self._numero_commande}:")
        for nom_plat, plat in self._plats_commandes.items():
            print(f"  - {nom_plat}: {plat['prix']} €")
        print(f"Total à payer: {total} €")

    # Méthode pour calculer la TVA
    def calculer_tva(self, taux_tva):
        total = self._calculer_total()
        tva = total * (taux_tva / 100)
        print(f"TVA ({taux_tva}%): {tva} €")

# Exemple d'utilisation
commande1 = Commande(1)

# Ajouter des plats à la commande
commande1.ajouter_plat("Canard aux olives", 20)
commande1.ajouter_plat("Mafé au boeuf", 18)
commande1.ajouter_plat("Romazava", 16)

# Afficher la commande
commande1.afficher_commande()

# Calculer la TVA
commande1.calculer_tva(10)

# Annuler la commande
commande1.annuler_commande()

# Afficher la commande annulée
commande1.afficher_commande()
