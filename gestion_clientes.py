#Proyecto-Final-IBM.JoséMaríaPachecoBenítez

# Sistema de Gestión de Clientes
# El propósito del ejercicio es desarrollar una aplicación para gestionar clientes.
# El sistema debe permitir agregar nuevos clientes, buscar clientes por nombre, listar todos los clientes y eliminar clientes

class Cliente:
    # Se define el constructor para añadir la información del cliente
    def __init__(self, nombre, email, telefono): 
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
    #Se implementa el método para mostrar la información de manera más amigable
    def __str__(self): 
        return f"Cliente: {self.nombre}, Email: {self.email}, Teléfono: {self.telefono}"
    
class SistemaClientes:
    def __init__(self):
        # Lista vacía donde se irán almacenando los clientes
        self.clientes = [] 
    
    def agregar_cliente(self, cliente):
        """" Añade un nuevo cliente al sistema."""
        self.clientes.append(cliente) # Añade el cliente a la lista
        print(f"Cliente {cliente.nombre} agregado con éxito.")

    def eliminar_cliente(self, nombre):
        """Elimina un cliente por su nombre."""
        cliente_encontrado = None # Variable generada para almacenar el cliente si lo encuentra
        for cliente in self.clientes:
            if cliente.nombre == nombre:
                cliente_encontrado = cliente
                break # si encontramos al cliente sale del bucle

        if cliente_encontrado:
            self.clientes.remove(cliente_encontrado) # elimina al cliente de la lista
            print(f"Cliente {nombre} eliminado con éxito.")
        else:
            print(f"Cliente {nombre} no encontrado.")

    def buscar_cliente(self, nombre):
        """Busca un cliente por su nombre."""
        for cliente in self.clientes:
            if cliente.nombre == nombre:
                return cliente # Devuelve el cliente si lo encuentra
        return None
    
    def listar_clientes(self):
        """Lista todos los clientes del sistema."""
        if not self.clientes:
            print("No hay clientes registrados.")
        else:
            for cliente in self.clientes:
                print(cliente) # realizada una llamda a __str__ de Cliente

# Implementando un sistema de elecciones con la función principal que contendrá el menú interactivo:

def main():
    sistema = SistemaClientes() # Creo una instancia del sistema de Clientes

    while True:
        # Muestra el menú de opciones
        print("======================================")
        print("--- Menú de Gestión de Clientes---")
        print("======================================")
        print("1. Agregar un cliente")
        print("2. Eliminar un cliente")
        print("3. Buscar un cliente")
        print("4. Listar todos los clientes en el sistema")
        print("5. Salir del sistema")
        print("======================================")
    
        # Leer la opción del usuario

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            # Se agrega un cliente
            nombre = input("Ingrese el nombre del cliente: ")
            email = input("Introduzca el correo electrónico del cliente: ")
            telefono = input("Introduzca el número de telefono del cliente: ")
            nuevo_cliente = Cliente(nombre, email, telefono) #crea un nuevo cliente
            sistema.agregar_cliente(nuevo_cliente) # lo agrega al sistema

        elif opcion == "2":
            # Elimina un cliente
            nombre = input("Introduzca el nombre del cliente a eliminar: ")
            sistema.eliminar_cliente(nombre) # se elimina al cliente del sistema por su nombre, si lo encuentra

        elif opcion == "3":
            # Búsqueda de un cliente por nombre
            nombre = input("Introduzca el nombre del cliente a buscar: ")
            cliente_encontrado = sistema.buscar_cliente(nombre) # busca al cliente por su nombre
            if cliente_encontrado:
                print(f"Cliente encontrado: {cliente_encontrado}")
            else:
                print(f"Cliente {nombre} no encontrad.")
        
        elif opcion == "4":
            # Listar todos los clientes
            sistema.listar_clientes()

        elif opcion == "5":
            # Salir del sistema
            print("Saliendo del sistema de gestión de clientes.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 5")


if __name__ == "__main__":
    main() # Con esto llamamos a la función principal para iniciar el programa


