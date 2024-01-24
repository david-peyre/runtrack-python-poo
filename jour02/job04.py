class Student:
    
    def __init__(self, nom, prenom, id_etudiant, credits=0):
        self._nom = nom
        self._prenom = prenom
        self._id_etudiant = id_etudiant
        self._credits = credits
        self._level = self._student_eval()

    def add_credits(self, nombre_credits):
        if nombre_credits > 0:
            self._credits += nombre_credits
            self._level = self._student_eval()
        else:
            print("Erreur : Le nombre de crédits ajouté doit être supérieur à zéro.")

    def _student_eval(self):
        if self._credits >= 90:
            return "Excellent"
        elif self._credits >= 80:
            return "Très bien"
        elif self._credits >= 70:
            return "Bien"
        elif self._credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        print(f"Nom = {self._nom}\nPrénom = {self._prenom}\nID = {self._id_etudiant}\nNiveau = {self._level}")

# Exemple d'utilisation
john_doe = Student("Doe", "John", 145)

# Ajouter des crédits à trois reprises
john_doe.add_credits(10)
john_doe.add_credits(10)
john_doe.add_credits(10)

# Imprimer le total de crédits en console
print(f"Le nombre de crédits de {john_doe._prenom} {john_doe._nom} est de {john_doe._credits} points.")

# Imprimer les informations de l'étudiant
john_doe.student_info()
