class Operation:

    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def get_values(self):
        return self.nombre1, self.nombre2


# Instanciation de la classe
operation_instance = Operation(12, 3)

# Utilisation de la méthode
nombre1, nombre2 = operation_instance.get_values()

# Impression des résultats
print("le nombre1 est", nombre1)
print("le nombre2 est", nombre2)
