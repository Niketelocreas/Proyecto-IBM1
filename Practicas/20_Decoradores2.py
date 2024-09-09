#20_Decoradores2


# Los decoradores vienen precedidos de un @
# Son funciones que se le añaden a otras funciones ya hecas.

# Función decoradora
def funcion_decoradora(funcion_a_decorar):

    def funcion_interior(num1, num2):
        print("El restulado es ")

        funcion_a_decorar(num1, num2)
    
        print(". Calculo terminado.")

    return funcion_interior

@funcion_decoradora
def suma(num1, num2):
    print(num1+num2)

@funcion_decoradora
def resta(num1, num2):
    print(num1-num2)

suma(3,5)
resta(10,4)
