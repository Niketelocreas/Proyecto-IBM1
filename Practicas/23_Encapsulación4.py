#23_Encapsulación4

# Encapsulación Básica con Atributos Privados

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def obtener_nombre(self): # Getter
        return self.__nombre # Con está función puedo obtener la variable privada Nombre porque está dentro de la clase
    
    def establecer_nombre(self, nombre): # Setter
        self.__nombre = nombre
        
    def obtener_edad(self):
        return self.__edad # Lo mismo con edad
    
    def establecer_edad(self, edad): 
        if edad > 0:
            self.__edad = edad
        else:
            print("La edad debe ser positiva")

# Uso
persona = Persona("Juan", 30)
print(persona.obtener_nombre())
persona.establecer_edad(35)
print(persona.obtener_edad())

# Se deben crear funciones que nos la enseñen funciones get - getter
# Para cambiarlos, se crean funciones de cambio, set - setter.
