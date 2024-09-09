#13_POO_Herencia2.1

# Herencia básica 

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def arrancar(self):
        return "El vehículo ha arrancado"

class Coche(Vehiculo):
    def __init__(self, marca, numero_puertas):
        super().__init__(marca) #El super lo que hace es usar la variable del constructor que viene de Vehiculo (el padre). Asi reutilizas
        self.numero_puertas= numero_puertas

    def abrir_puertas(self):
        return f"Abrir {self.numero_puertas} puertas"
    
class CocheElectrico(Coche):
    def __init__(self, marca, numero_puertas, voltaje):
        super().__init__(marca, numero_puertas) #El super lo hereda del padre, no del abuelo
        self.voltaje = voltaje 

    
# Uso
mi_coche = Coche("Toyota", 4)
print(mi_coche.marca) # Hereda el atributo marca
print(mi_coche.arrancar()) # Hereda el método arrancar
print(mi_coche.numero_puertas)
print(mi_coche.abrir_puertas())