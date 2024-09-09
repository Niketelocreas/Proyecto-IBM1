#21_Decoradores3


# Los decoradores vienen precedidos de un @
# Son funciones que se le añaden a otras funciones ya hecas.

# Función decoradora
def funcion_decoradora(funcion_a_decorar):

    def funcion_interior(*args):
        print("El restulado es ")

        funcion_a_decorar(*args)
    
        print(". Calculo terminado.")

    return funcion_interior

@funcion_decoradora
def suma(num1, num2):
    print(num1+num2)

@funcion_decoradora
def resta(num1, num2):
    print(num1-num2)

@funcion_decoradora
def multiplica(num1, num2, num3):
    print(num1*num2*num3)

suma(3,5)
resta(10,4)
multiplica(2, 3, 4)