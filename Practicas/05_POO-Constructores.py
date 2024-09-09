# POO-Constructores

# Clase Básica de un círculo

import math

class Circulo: # Clase sin variables, solo con 3 métodos.
    def __init__(self, radio):  # equivaldría a inicializar una variable radio tipo: radio = 19 (pero todos tendrían el mismo radio)
        self.radio = radio
    
    def area(self):
        return math.pi* self.radio**2
    
    def perimetro(self):
        return 2* math.pi *self.radio
    
# Uso
miCirculo = Circulo(5)
print("El área es: ", miCirculo.area())
print("El perímetro es: ", miCirculo.perimetro())
