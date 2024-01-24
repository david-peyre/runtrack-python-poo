class Livre:

    def __init__(self, titre, auteur, nombre_pages):
        self._titre = titre
        self._auteur = auteur
        self._nombre_pages = nombre_pages

    # Accesseurs (getters)
    def getTitre(self):
        return self._titre

    def getAuteur(self):
        return self._auteur

    def getNombrePages(self):
        return self._nombre_pages

    # Mutateurs (setters)
    def setTitre(self, nouveau_titre):
        self._titre = nouveau_titre

    def setAuteur(self, nouveau_auteur):
        self._auteur = nouveau_auteur

    def setNombrePages(self, nouveau_nombre_pages):
        # Vérification pour s'assurer que le nombre de pages est un entier positif
        if isinstance(nouveau_nombre_pages, int) and nouveau_nombre_pages > 0:
            self._nombre_pages = nouveau_nombre_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

# Exemple d'utilisation
livre1 = Livre("Le rouge et le noir", "Stendhal", 512)

# Afficher les valeurs initiales
print("Titre :", livre1.getTitre())
print("Auteur :", livre1.getAuteur())
print("Nombre de pages :", livre1.getNombrePages())

# Changer les valeurs
livre1.setTitre("L'éthique")
livre1.setAuteur("Spinoza")
livre1.setNombrePages(640)

# Afficher les nouvelles valeurs
print("\nNouveau titre :", livre1.getTitre())
print("Nouvel auteur :", livre1.getAuteur())
print("Nouveau nombre de pages :", livre1.getNombrePages())

# Essayer de changer le nombre de pages avec des valeurs invalides
livre1.setNombrePages("pommes")
livre1.setNombrePages(-1)
livre1.setNombrePages(2.3)

