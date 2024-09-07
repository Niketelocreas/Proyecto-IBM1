# Programa que pide una nota por consola y valora si el alumno ha aprobado o no.

notaIn = int(input("Introduce tu nota: "))

if notaIn < 5:
    calificacion="suspenso"
else: calificacion="aprobado"

print(calificacion)

# If no solo evalua un booleano, también si una variable contiene información

variable = 19

if variable: # que en realidad es una simplifacion de if variable == True:
    print("Contiene información")
else:
    print("No contiene información")

# Programa que pide una edad por consola y valora si el usuario es mayor de edad o no

edad = int(input("Introduce tu edad: "))
if edad < 18:
    print("No puedes pasar")
elif edad>100:
    print("Disfruta de la marcha")
else: 
    print("Adelante, pero bebe con moderación")

# Mejorando el programa de la nota

nota=int(input("Introduce tu nota: "))

if nota<5:
    print("Suspenso")
elif nota<7:
    print("Aprobado")
elif nota<9:
    print("Notable")
else:
    print("Sobresaliente")

# IF abreviado

n_num1 = 5
n_num2 = 10
if n_num1 > n_num2: print(n_num1, "es mayor que", n_num2)

# If.. Else abreviado
a = 2
b = 330
print("A") if a > b else print("B")

# En realidad es mucho mas legible asi:

if a>b:
    print("A")
else: 
    print("B")

# se pueden concatenar operadores de comparación:
edad2 = 117
if 0<edad2<100: # seria como poner: if edad>0 and edad<100
    print("Edad correcta")
else:
    print("Edad incorrecta")
    

