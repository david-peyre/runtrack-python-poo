class CompteBancaire:

    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self._numero_compte = numero_compte
        self._nom = nom
        self._prenom = prenom
        self._solde = solde
        self._decouvert = decouvert

    def afficher(self):
        print(f"Compte #{self._numero_compte}: {self._prenom} {self._nom}")
        print(f"Solde actuel: {self._solde} €")
        print(f"Prêt autorisé: {self._decouvert}")
        print()

    def afficher_solde(self):
        print(f"Solde actuel: {self._solde} €")

    def versement(self, montant):
        self._solde += montant
        print(f"Versement de {montant} € effectué. Nouveau solde: {self._solde} €")

    def retrait(self, montant):
        if self._solde - montant >= 0 or self._decouvert:
            self._solde -= montant
            print(f"Retrait de {montant} € effectué. Nouveau solde: {self._solde} €")
        else:
            print("Opération impossible. Solde insuffisant.")

    def agios(self, taux_agios):
        if self._solde < 0:
            agios = abs(self._solde) * (taux_agios / 100)
            self._solde -= agios
            print(f"Agios de {agios} € appliqués. Nouveau solde: {self._solde} €")
        else:
            print("Pas d'agios à appliquer.")

    def virement(self, compte_destinataire, montant):
        if self._solde - montant >= 0 or self._decouvert:
            self._solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} € effectué. Nouveau solde: {self._solde} €")
        else:
            print("Opération impossible. Solde insuffisant.")

# Créer un compte 
compte1 = CompteBancaire(1, "Doe", "John", 5000)

# Faire appel aux différentes méthodes
compte1.afficher()
compte1.versement(2000)
compte1.retrait(1000)
compte1.agios(2)

# Ajouter l’attribut decouvert à la classe CompteBancaire
compte2 = CompteBancaire(2, "Dupont", "Alice", -1000, decouvert=True)

# Deuxième instance de la classe CompteBancaire
compte2.afficher()

# Faire un versement du premier compte vers celui à découvert afin de le remettre à zéro
compte1.virement(compte2, 3000)

# Afficher les états des comptes après le virement
compte1.afficher()
compte2.afficher()
