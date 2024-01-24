class Tache:
    
    def __init__(self, titre, description, statut="À faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"{self.titre} - {self.description} - Statut: {self.statut}"


class ListeDeTaches:

    def __init__(self):
        self.taches = []

    def ajouter_tache(self, tache):
        self.taches.append(tache)
        print(f"Tâche ajoutée: {tache}")

    def supprimer_tache(self, titre):
        tache_a_supprimer = None
        for tache in self.taches:
            if tache.titre == titre:
                tache_a_supprimer = tache
                break

        if tache_a_supprimer:
            self.taches.remove(tache_a_supprimer)
            print(f"Tâche supprimée: {tache_a_supprimer}")
        else:
            print(f"Tâche non trouvée avec le titre {titre}")

    def marquer_comme_finie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "Terminée"
                print(f"Tâche marquée comme terminée: {tache}")
                break

    def afficher_liste(self):
        print("Liste des tâches:")
        for tache in self.taches:
            print(tache)

    def filter_liste(self, statut):
        taches_filtrees = [tache for tache in self.taches if tache.statut == statut]
        print(f"Tâches avec le statut {statut}:")
        for tache in taches_filtrees:
            print(tache)


# Tester le code
tache1 = Tache("Faire les courses", "Acheter du pain et du lait")
tache2 = Tache("Réviser Python", "Préparer pour l'examen")
tache3 = Tache("Faire du sport", "Courir pendant 30 minutes")
tache4 = Tache("Réunion", "Réunion d'équipe", "Terminée")

liste_taches = ListeDeTaches()

# Ajouter des tâches
liste_taches.ajouter_tache(tache1)
liste_taches.ajouter_tache(tache2)
liste_taches.ajouter_tache(tache3)
liste_taches.ajouter_tache(tache4)

# Afficher la liste des tâches
liste_taches.afficher_liste()

# Marquer une tâche comme terminée
liste_taches.marquer_comme_finie("Réunion")

# Afficher la liste mise à jour
liste_taches.afficher_liste()

# Supprimer une tâche
liste_taches.supprimer_tache("Faire les courses")

# Afficher la liste mise à jour
liste_taches.afficher_liste()

# Filtrer les tâches par statut
liste_taches.filter_liste("À faire")
