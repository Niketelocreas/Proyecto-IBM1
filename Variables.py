# Variables

# Lo ideal es declarar e inicializar siempre las variables.
# -------------------------------------------------------

# Declaración de una variable númerica entera
n_edad = 47
numero = n_edad+1

print(numero)
# Declaración de una variable númerica flotante:
n_numero = -23.43

# Declaración de una variable de tipo string:

s_numero = 'Manolo es "amigo" mío' # Es importante alternar las comillas simples y dobles para que no haya lios
print(s_numero) # De esta manera consigues tener una frase entrecomillada

# Declaraciónd e variable de tipo string en varias líneas:
s_textolargo = """Esto es un mensaje
... con tres saltos
... de línea"""
# Al usar las tres dobles comillas provoca un salto de línea

# Esto también puede conseguirse con \n entre comillas dobles
s_textolargo2 = "Esto es un mensaje \ncon tres saltos \nde linea"

print(s_textolargo)
print(s_textolargo2)
# Sobreescribir el valor de la variable s_edad y ahora ponerlo como string:
s_edad = "47"
print(s_edad)


# Declaración de una constante - Al declarar una constante Python no te va a permitir modificarla.
# Para ello se pone el nombre en mayusculas
NUMEROPI = 3.14159

# Declaración de un booleano
is_verdadero = True
is_casado = False

# True y False como valores
True == 1
False == 0
print (True + 2)
