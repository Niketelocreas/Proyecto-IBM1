#10_POO_Herencia3

# Herencia básica

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

class Estudiante(Persona):
    pass

class Profesor(Persona):
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años y soy profesora de matemáticas."

# Uso
estudiante = Estudiante("Ana", 21)
print(estudiante.nombre) # Hereda el atributo nombre
print(estudiante.edad) # Hereda el atributo edad
print(estudiante.saludar()) # Hereda el método saludar

estudiante2 = Estudiante("Miguel", 29)
print(estudiante2.nombre) # Hereda el atributo nombre
print(estudiante2.edad) # Hereda el atributo edad
print(estudiante2.saludar()) # Hereda el método saludar

estudiante3 = Estudiante("Juana", 12)
print(estudiante3.nombre) # Hereda el atributo nombre
print(estudiante3.edad) # Hereda el atributo edad
print(estudiante3.saludar()) # Hereda el método saludar

profesor = Profesor("Maria Antonia", 44)
print(profesor.nombre)
print(profesor.edad)
print(profesor.saludar())