# Programación Orientada a Objetos

# El ejemplo a continuación tiene que refinarse, no se hace así exactamente.
class Coche():
    # Declaración de atributos
    largo = 250
    ancho = 120
    ruedas = 4
    peso = 900
    color = "rojo"
    is_enMarcha = False

    # Declaración de métodos
    def arrancar(self): #self hace referencia a la instancia de clase.
        self.is_enMarcha = True # es como si pusiésemos el miCoche.is_enMarcha = True

    def estado(self):
        if (self.is_enMarcha == True):
            return "El coche está arrancado"
        else:
            return "El coche está parado"
# Declaración de una instancia de clase, objeto de clase o ejemplo
miCoche = Coche()
miCoche2 = Coche()

# Acceso a un atributo de la clase Coche. Nomenclatura del punto.
print("El largo del coche es de ", miCoche.largo, "cm.")
print(miCoche.estado())
miCoche.arrancar()
print(miCoche.color)


# Acceso a un método de la clase Coche. Nomenclatura del punto.
print("El coche está arracado:", miCoche.arrancar())

#Modificamos el valor de una propiedad
miCoche2.ruedas= 10
print("El coche2 tiene: ", miCoche2.ruedas, "ruedas.")