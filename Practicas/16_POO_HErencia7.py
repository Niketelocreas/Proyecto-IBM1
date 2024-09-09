#16_POO_HErencia7

# Herencia con Métodos Adicionales y Atributos (Empleado y Programador)

class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def detalles(self):
        return f"Empleado: {self.nombre}, Edad: {self.edad}, Salario: {self.salario}"

class Programador(Empleado):
    def __init__(self, nombre, edad, salario, lenguajes):
        super().__init__(nombre, edad, salario)  # Llama al constructor de Empleado
        self.lenguajes = lenguajes  # Añade lenguajes como atributo adicional

    def detalles(self):
        return f"Programador: {self.nombre}, Edad: {self.edad}, Salario: {self.salario}, Lenguajes: {', '.join(self.lenguajes)}"

    def agregar_lenguaje(self, lenguaje):
        self.lenguajes.append(lenguaje)

# Uso
empleado = Empleado("Júan Pérez", 30, 50000)
programador = Programador("Antonia Gómez", 39, 70000, ["Python", "Javascript"])  # Ahora usa la clase correcta
print(empleado.detalles())
print(programador.detalles())
programador.agregar_lenguaje("Java")
print(programador.detalles())