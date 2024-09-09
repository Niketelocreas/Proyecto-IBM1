#15_POO_Herencia2.2

# Herencia con Métodos Sobreescritos (Vehículo, Coche y Bicicleta)

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"{self.marca} {self.modelo}"
    
    def tipo(self):
        pass

class Coche(Vehiculo):
    def __init__(self, marca, modelo, numero_puertas):
        super().__init__(marca, modelo) #El super lo que hace es usar la variable del constructor que viene de Vehiculo (el padre). Asi reutilizas
        self.numero_puertas= numero_puertas

    def tipo(self):
        return "Coche"
    
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo_bicicleta):
        super().__init__(marca, modelo) 
        self.tipo_bicicleta = tipo_bicicleta

    def tipo(self):
        return "Bicicleta"
    
# Uso
mi_coche = Coche("Toyota", "Corolla", 4)
mi_bici= Bicicleta("Giant", "Escape 3", "Híbrida")
print(mi_coche.marca) # Hereda el atributo marca
print(mi_coche.descripcion(), "-", mi_coche.tipo()) # Hereda el método arrancar
print(mi_bici.descripcion(), "-", mi_bici.tipo())