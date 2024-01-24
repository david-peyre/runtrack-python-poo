class Voiture:

    def __init__(self, marque, modele, annee, kilometrage, en_marche=False):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._kilometrage = kilometrage
        self._en_marche = en_marche
        self._reservoir = 50

    # Assesseurs (getters)
    def get_marque(self):
        return self._marque

    def get_modele(self):
        return self._modele

    def get_annee(self):
        return self._annee

    def get_kilometrage(self):
        return self._kilometrage

    def get_en_marche(self):
        return self._en_marche

    # Mutateurs (setters)
    def set_marque(self, nouvelle_marque):
        self._marque = nouvelle_marque

    def set_modele(self, nouveau_modele):
        self._modele = nouveau_modele

    def set_annee(self, nouvelle_annee):
        self._annee = nouvelle_annee

    def set_kilometrage(self, nouveau_kilometrage):
        self._kilometrage = nouveau_kilometrage

    def set_en_marche(self, nouvel_etat):
        self._en_marche = nouvel_etat

    # Méthodes publiques
    def demarrer(self):
        if self._verifier_plein() > 5:
            self._en_marche = True
            print("La voiture démarre.")
        else:
            print("La voiture ne peut pas démarrer, réservoir trop bas.")

    def arreter(self):
        self._en_marche = False
        print("La voiture s'arrête.")

    # Méthode privée
    def _verifier_plein(self):
        return self._reservoir

# Exemple d'utilisation
ma_voiture = Voiture("Toyota", "Corolla", 2020, 20000)

# Accéder aux informations initiales
print("Marque :", ma_voiture.get_marque())
print("Modèle :", ma_voiture.get_modele())
print("Année :", ma_voiture.get_annee())
print("Kilométrage :", ma_voiture.get_kilometrage())
print("En marche :", ma_voiture.get_en_marche())

# Démarrer la voiture
ma_voiture.demarrer()

# Accéder à l'état de la voiture après démarrage
print("En marche après démarrage :", ma_voiture.get_en_marche())

# Arrêter la voiture
ma_voiture.arreter()

# Accéder à l'état de la voiture après arrêt
print("En marche après arrêt :", ma_voiture.get_en_marche())
