#17_POO_Herencia2.3

# Herencia Múltiple Básica

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def detalles(self):
        return f"Vehículo: {self.marca}"
        
class Motor:
    def __init__(self, tipo_motor):
        self.tipo_motor = tipo_motor

    def detalles(self):
        return f"Motor: {self.tipo_motor}"
class Coche(Vehiculo, Motor):
    def __init__(self, marca, tipo_motor, modelo):
        Vehiculo.__init__(self, marca) #Aqui no usa super, sino la clase en particular, de lo contrario entraría en conflicto
        Motor.__init__(self, tipo_motor)
        self.modelo = modelo 
         
    def descripcion(self):
        return f"{self.marca} {self.modelo} con motor {self.tipo_motor}"

    def detalles(self):
        return f"Vehículo: {self.marca}, Motor: {self.tipo_motor}"
# Uso
coche = Coche("Toyota", "V6", "Corolla")
print(coche.descripcion())
print(coche.detalles()) # Muestra la versión sobre escrita del hijo, no la del Padre1 o Padre2
 # Si no estuviese sobrescrito, habría cogido el de Vehículo, porque es el que está primero
