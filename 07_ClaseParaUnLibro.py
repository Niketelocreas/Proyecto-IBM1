# Clase Para Un Libro

class Libro:
    # Se introduce el método constructor para poder introducir las instancias una vez se haga la llamada a la clase
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
    
    def descripcion(self):
        return f" '{self.titulo}' por {self.autor} ({self.anio_publicacion})"
    
    def es_antiguo(self):
        return self.anio_publicacion < 2000
    
# Uso

libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)
print(libro1.descripcion())
print("¿Es antiguo?", libro1.es_antiguo())