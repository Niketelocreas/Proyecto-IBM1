# 11_POO_Herencia4

# Crea una clase base llamada SerVivo con un método respirar que devuelva "estoy respirando"
# Luego, crea una clase derivada llamada Animal que herede de SerVivo y añada un método que devuelva "me estoy moviendo"
# Finalmente, crea una clase derivada llamada Perro que herede de Animal y sobrescriba el método moverse para devolver "estoy corriendo"
# Crea una instancia de Perro y muestra los resultados

class SerVivo:
    def respirar(self):
        return "Estoy respirando"
    
class Animal(SerVivo):
    def moverse(self):
        return "Me estoy moviendo"

class Perro(Animal):
    def moverse(self):
        return "Estoy corriendo"
    
# Instancia
mi_perro = Perro()

# mostrar métodos

print(mi_perro.respirar())
print(mi_perro.moverse())