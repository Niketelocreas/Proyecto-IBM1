#22_Encapsulación1
# Encapsular nos permite hacer intocables las variables dentro de una función
# Formas de encapsular. poniendo delante de la palabra public, o private o protected (en otros lenguajes)
# En python se trabaja con dos barras bajas __ para protejerlas (encapsularlas)
# Si solo tiene una barra baja _ es como un mensaje del programador para que no lo cambies

class Coche():
    largo = 250

    # Método constructor
    def __init__(self):
        self.__largo = 250
        self.__ancho = 120
        self.__ruedas = 4
        self.__peso = 880
        self.__color = "rojo"
        self.__is_enMarcha = False

    # Declaración de métodos
    def arrancar(self):  # Hace referencia a la instancia de clase
        self.__is_enMarcha = True  # Es como si pusiesemos miCoche.__is_enMarcha = True

    def estado(self):
        if self.__is_enMarcha:
            return "El coche está arrancado"
        else:
            return "El coche está parado"

    # Método para obtener las ruedas
    def get_ruedas(self):
        return self.__ruedas

# Declaración de una instancia de clase, objeto de clase o ejemplar
miCoche = Coche()
print("Mi coche tiene", miCoche.get_ruedas(), "ruedas.")  # Ahora accedemos al método para obtener las ruedas
help(Coche)
