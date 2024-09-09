#12_POO_Herencia5


class Dispositivo:
    def encender(self):
        return "El dispositivo está encendido"
    
class Computadora(Dispositivo):
    def procesar_datos(self):
        return "Procesando datos"
    

class Laptop(Computadora):
    def procesar_datos(self):
        return "Procesando datos en el laptop"

# Crear instancia y mostrar métodos

mi_laptop = Laptop()

print(mi_laptop.encender())
print(mi_laptop.procesar_datos())