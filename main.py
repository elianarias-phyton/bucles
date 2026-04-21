##NIVEL 1
from random import random
from time import time

#EJERCICIO 1

# texto = input("Introduzca un texto: ")
#
# for i in range(20):
#     print(texto)

#EJERCICIO 2

# numero = int(input("Introduzca un número: "))
#
# for i in range(numero):
#     print("*", end= "")

#EJERCICIO 3

# texto = input("Introduzca un texto: ")
# numero = int(input("Introduzca un número: "))
#
# for i in range(numero):
#     print(texto)

#EJERCICIO 4

# for i in range(0,101,2):
#     print(i)

##NIVEL 2

#EJERCICIO 5

# suma = 0
#
# for i in range(1,101):
#     suma = suma + i
#     print(suma)

#EJERCICIO 6

# suma = 0
#
# for i in range(0,101,2):
#     suma = suma + i
#     print(suma)

#EJERCICIO 7

# suma = 0
#
# for i in range(0,201,1):
#     suma = suma + i
#     print(suma)
#
# print("Se sumaron un total de" ,i, "numeros.")

#EJERCICIO 8

# numero = int(input("Introduzca un número: "))
#
# for i in range(1,11):
#     print(numero ,"x", i , "=" , numero * i)

#NIVEL 3

#EJERCICIO 9

# promedio = 0
#
# for i in range(10):
#     notas = float(input("Ingresa todas las notas y te digo el promedio: "))
#     while notas > 10 or notas < 0:
#         notas = float(input("Nota fuera del rango. Ingrese nuevamente: "))
#
#     promedio = promedio + notas
#
# p = f"{promedio:.2f}"
#
# print("Su promedio final es de: " , p/10)

#EJERCICIO 10

# acum = 0
#
# for i in range (3):
#     numero = int(input("Introduzca números: "))
#     acum = acum + numero
#
# print("La suma total de los numeros introducidos es: " , acum)
# print("El promedio total de los numeros introducidos es: " , acum/3)

#EJERCICIO 11

# numero_1 = int(input("Introduzca un número: "))
# numero_2 = int(input("Introduzca otro número: "))
#
# for i in range (numero_1+1,numero_2,1):
#     print(i)

#NIVEL 4

#EJERCICIO 12

# numero = 0
# contador = 0
# suma = 0
#
# while numero != -1:
#     numero = float(input("Ingrese numeros aleatorios, cuando ingrese -1 se van a promediar todos: "))
#
#     if numero != -1:
#         suma = suma + numero
#         contador = contador + 1
#
# promedio = suma / contador
#
# print("El promedio es: ", promedio)

#EJERCICIO 13

# numero = 0
# contador = 0
#
# while numero != -1:
#     numero = float(input("Ingrese numeros aleatorios, te voy a decir cuantos 10 pusiste, pone -1 y termina: "))
#
#     if numero == 10:
#         contador = contador + 1
#
# print("Colocó el número 10 unas" , contador , "veces.")

#EJERCICIO 14

# palabras = 0
#
# while palabras != "SALIR":
#     palabras = input("Ingrese palabras aleatorias, para salir del bucle escriba SALIR: ")
#
# print("Lograste salir del bucle.")

#NIVEL 5

#EJERCICIO 15

# alumnos = 0
#
# cupo = int(input("Inserte el cupo máximo del curso: "))
#
# while alumnos < cupo:
#     input("Ingrese el nombre del alumno: ")
#     alumnos = alumnos + 1
#
# print("El curso ha alcanzado su capacidad máxima")

#EJERCICIO 16

# ingresos =  0
#
# objetivo = int(input("Inserte el valor del objetivo: "))
#
# while ingresos < objetivo:
#     dinero = int(input("Ingrese sus ingresos: "))
#     ingresos = ingresos + dinero
#     if ingresos > objetivo:
#         resto = ingresos - objetivo
#         print("Alcanzo el objetivo de ahorro y le sobraron:" ,resto,)
#     else:
#         print("Se alcanzó el objetivo de ahorro.")


#EJERCICIO 17

# nombre = input("Ingrese el nombre del producto: ")
# precio = int(input("Ingrese el precio del producto: "))
# stock = int(input("Ingrese el stock del producto: "))
#
# print("Su producto es" , nombre, "el precio es de $" , precio , "y el stock actual es de " , stock)
#
# while stock > 4:
#     ventas = int(input("Ingrese el numero de ventas del producto: "))
#     stock = stock - ventas
#
# print("Para poder seguir realizando ventas debe reponer el stock.")

#NIVEL 6

#EJERCICIO 18

# numero = int(input("Ingrese un numero: "))
#
# for i in range(1,numero+1,1):
#     print("*"*i)
# for i in range(numero-1,0,-1):
#     print("*"*i)

#EJERCICIO 19

# numero = int(input("Ingrese el numero 4: "))
#
# for i in range(1,numero+1,1):
#     print(end="*")
# print()
#
# for i in range(1, numero + 1, 1):
#     print("*", numero*"" , "*")
#
# for i in range(1, numero+1, 1):
#     print(end="*")

#EJERCICIO 20

# import random
# numero_aleatorio = random.randint(1, 100)
# intentos = 10
#
# print("Bienvenido al juego de las adivinanzas.")
# print("Tenés 10 intentos para adivinar el numero oculto.")
#
# numero_usuario = int(input("Intente adivinar el número oculto entre 1 y 100: "))
#
# while numero_usuario != numero_aleatorio:
#
#     if numero_usuario < numero_aleatorio:
#         numero_usuario = int(input("Le erraste, el numero oculto es MAYOR, insertá otro número: "))
#         intentos = intentos -1
#         print(intentos , "restantes.")
#         if intentos == 0:
#             print("Te quedaste sin intentos. Fin del juego.")
#             break
#     elif numero_usuario > numero_aleatorio:
#         numero_usuario = int(input("Le erraste, el numero oculto es MENOR, insertá otro número: "))
#         intentos = intentos - 1
#         print(intentos, "restantes.")
#         if intentos == 0:
#             print("Te quedaste sin intentos. Fin del juego.")
#             break
# else:
#     print("¡Ganaste! El numero random era", numero_aleatorio)