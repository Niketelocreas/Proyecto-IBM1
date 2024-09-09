#14_POO_Herencia6

# Crea una clase base llamada Animal, con un atributo nombre y un metodo hacer sonido
# Luego, crea una derivada llamada Perro que herede Animal y añada un atributo raza
# y un método ladrar. Crea una instancia Perro y muestra atributos y métodos.

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "Algún sonido genérico"

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def ladrar(self):
        return "Guau, guau"
    
# Crear una instancia de Perro
mi_perro = Perro("Firulais", "Labrador")

print(mi_perro.nombre)
print(mi_perro.hacer_sonido())
print(mi_perro.raza)
print(mi_perro.ladrar())
