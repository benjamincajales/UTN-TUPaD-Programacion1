#alumno: Benjamin Cajales
#TP4

#1- Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#debera mostrar un mensaje en pantall que diga "Es mayor de edad".

i = 0
for i in range(100):
    print(i)

#2- Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6,
#debera mostrar por pantalla un mensaje que diga "Aprobado"; en caso contrario debera mostrar el mensaje "Desaprobado"

numero = int(input("ingrese un numero entero: "))
contador = 0
b = numero
while b > 0:
    a = b % 10
    if a >= 0:
        contador = contador + 1
    b = b // 10
print("Digitos que contiene este numero es: ",contador)

#3- Escribir un programa que permita ingresar solo numeros pares. Si el usuario ingresa un numero par,
#imprimir en pantalla el mensaje "Ha ingresado un numero par", en caso contrario, imprimir por pantalla 
# "Por favor, ingrese un numero par"

extremo_bajo = int(input("ingrese el extremo mas bajo: "))
extremo_alto = int(input("ingrese el extremo mas alto: "))
suma_total = 0
for i in range(extremo_bajo + 1,extremo_alto):
    print(i)
    suma_total = suma_total + i
print("")
print(suma_total)

#4- Escribir un programa que solicite al usuario su edad e imprima por pantalla a cual de las siguientes 
#categorias pertenece:
#niño/a:  < 12 años, adolescente: >= 12 años and < 18 años, adulto/a joven: >= 18 años and < 30 años, adulto/a: >= 30 años

valor_verdad = True
sumatoria = 0
print("Para salir del bucle coloque 0")
while valor_verdad == True:
    numero = int(input("ingrese un numero entero: "))
    sumatoria = sumatoria + numero
    if numero == 0:
        valor_verdad = False
print("Total sumados es: ",sumatoria)

#5- Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14)

import random
numero_random = random.randint(0,9)
numero = None
contador = 0
print(numero_random)
print("")
while numero != numero_random:
    numero = int(input("ingrese un numero [0-9]: "))
    contador = contador + 1
print("Intentos de adivinar el numero es: ",contador)

#ejercicio 6

for i in range(100,0,-1):
    if i % 2 == 0:
        print(i)

#ejercicio 7

numero_limite = int(input("ingrese un numero entero positivo: "))
if numero_limite < 0 or numero_limite % 2 != 0:
    while numero_limite % 2 != 0:
        numero_limite = int(input("incorrecto, ingrese un numero entero positivo: "))
suma = 0
for i in range(numero_limite + 1):
    print(i)
    suma = i + suma
print("")
print(suma)

#ejercicio 8

pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(1,101):
    numero = int(input(f"ingrese el numero {i}: "))
    #determinamos si el numero es positivo o negativo
    if numero > 0:
        positivos = positivos + 1
    elif numero < 0:
        negativos = negativos + 1
    #determinamos si el numero es par o impar
    if numero % 2 == 0:
        pares = pares + 1
    elif numero % 2 != 0:
        impares = impares + 1
print("Hay: ")
print(f"pares: {pares}, impares: {impares}, positivos: {positivos} y negativos: {negativos}") 

#ejercicio 9

media: int = 0
promedio: float = 0
for i in range(1, 101):
    numero = int(input(f"ingrese el numero {i}: "))
    media = media + numero
promedio = media / i
print(f"El promedio de los {i} numeros es: {promedio}")

#ejercicio 10

numero = int(input("ingrese un numero: "))
invertido = 0
numero_cambiado = numero
while numero_cambiado > 0:
    ultimo_digito = numero_cambiado % 10
    invertido = (invertido * 10) + ultimo_digito
    numero_cambiado = int(numero_cambiado / 10)
print(f"La inversa del numero {numero} es: {invertido}")