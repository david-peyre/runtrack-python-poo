class Ville:
    def __init__(self, nom, nombre_habitants):
        self._nom = nom
        self._nombre_habitants = nombre_habitants

    def get_nombre_habitants(self):
        return self._nombre_habitants

    def augmenter_population(self):
        self._nombre_habitants += 1


class Personne:

    def __init__(self, nom, age, ville):
        self._nom = nom
        self._age = age
        self._ville = ville
        # Ajouter la personne à la population de la ville
        self._ville.augmenter_population()


# Créer Paris, 1000000 hab
paris = Ville("Paris", 1000000)
# Afficher le nombre d’habitants de Paris
print(f"Population de la ville de Paris : {paris.get_nombre_habitants()}")

# Créer Marseille, 861635 hab
marseille = Ville("Marseille", 861635)
# Afficher le nombre d’habitants de Marseille
print(f"Population de la ville de Marseille : {marseille.get_nombre_habitants()}")

# Créer les objets personnes
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Afficher le nombre d’habitants de Paris et de Marseille après l’arrivée des nouvelles personnes
print(f"Population de la ville de Paris mise à jour : {paris.get_nombre_habitants()}")
print(f"Population de la ville de Marseille mise à jour : {marseille.get_nombre_habitants()}")
