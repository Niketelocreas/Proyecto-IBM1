#08_POO_Herencia1

# Herencia básica Animal y Perro

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"
    
# Uso
perro = Perro("Firulais") # de esta forma coge el atributo nombre del padre. En la clase hija se ha modificado el hacer sonido y se ha puesto guau
print(perro.nombre)
print(perro.hacer_sonido())