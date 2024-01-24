class Livre:

    def __init__(self, titre, auteur, nombre_pages):
        self._titre = titre
        self._auteur = auteur
        self._nombre_pages = nombre_pages
        self._disponible = True

    # Accesseurs (getters)
    def getTitre(self):
        return self._titre

    def getAuteur(self):
        return self._auteur

    def getNombrePages(self):
        return self._nombre_pages

    def verification(self):
        return self._disponible

    def emprunter(self):
        if self._disponible:
            self._disponible = False
            print("Livre emprunté avec succès.")
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

    def rendre(self):
        if not self._disponible:
            self._disponible = True
            print("Livre rendu avec succès.")
        else:
            print("Le livre n'a pas été emprunté. Impossible de le rendre.")

# Exemple d'utilisation
livre1 = Livre("Le rouge et le noir", "Stendhal", 512)

# Afficher la disponibilité initiale
print("Le livre est disponible :", livre1.verification())

# Emprunter le livre
livre1.emprunter()

# Vérifier à nouveau la disponibilité
print("Le livre est disponible :", livre1.verification())

# Rendre le livre
livre1.rendre()

# Vérifier à nouveau la disponibilité
print("Le livre est disponible :", livre1.verification())
