#Otras Creaciones De Clases

# Clase sin constructor

class Persona:
    pass # El pass solo sirve cuando dejas la clase vacía

# Crear una instancia de la clase Persona
persona = Persona()

# Agregar atributos a la instancia
persona.nombre = "Ana"
persona.edad = 30

# Definir un método para la clase
def presentarse(self):
    return f"Hola, soy {self.nombre} y tengo {self.edad} años."
    
 # Asociar el método a la instancia
Persona.presentarse = presentarse
print(persona.presentarse())    