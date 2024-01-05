class Operation:

    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def get_values(self):
        return self.nombre1, self.nombre2
    
    def addition(self):
        return self.nombre1 + self.nombre2


# Instanciation de la classe
operation_instance = Operation(12, 3)

# Utilisation de la méthode addition sur l'instance de la classe
result_addition = operation_instance.addition()
print("Le résultat de l'addition de nombre1 et nombre2 est", result_addition)
