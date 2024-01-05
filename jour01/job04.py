class Personne:

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return "Je suis {} {}".format(self.prenom, self.nom)


# Instanciation des personnes
p1 = Personne("John", "Doe")
p2 = Personne("Antoine", "Dupont")

# Appel de la méthode SePresenter et impression des résultats
print(p1.SePresenter())
print(p2.SePresenter())
