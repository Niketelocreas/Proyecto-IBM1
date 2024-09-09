#19_Decoradores

# Los decoradores vienen precedidos de un @
# Son funciones que se le añaden a otras funciones ya hecas.

# Función decoradora
def funcion_decoradora(funcion_a_decorar):

    def funcion_interior():
        print("El restulado es ")

        funcion_a_decorar()
    
        print(". Calculo terminado.")

    return funcion_interior

@funcion_decoradora
def suma():
    print(15+20)

@funcion_decoradora
def resta():
    print(30-10)

suma()
resta()

