#alumno: Benjamin Cajales
#TP3

#1- Crea un programa que imprima en pantalla todos los numeros enteros desde 0 hasta 100 (incluidos),
# en orden creciente, mostrando un numero por linea.

i = 0
for i in range(100):
    print(i)

#2- Desarrolla un programa que solicite al usuario un numero entero y determine la cantidad de digitos que contiene 

numero = int(input("ingrese un numero entero: "))
contador = 0
b = numero
while b > 0:
    a = b % 10
    if a >= 0:
        contador = contador + 1
    b = b // 10
print("Digitos que contiene este numero es: ",contador)

#3- Escribe un programa que sume todos los numeros enteros comprendidos entre 2 valores dados por el usuario (excluidos extremos).

extremo_bajo = int(input("ingrese el extremo mas bajo: "))
extremo_alto = int(input("ingrese el extremo mas alto: "))
suma_total = 0
for i in range(extremo_bajo + 1,extremo_alto):
    print(i)
    suma_total = suma_total + i
print("")
print(suma_total)

#4- Escribe un programa que permita al usuario ingresar numeros enteros y los sume en secuencia.
# El programa debe detenerse y mostrar el total acumulado.

valor_verdad = True
sumatoria = 0
print("Para salir del bucle coloque 0")
while valor_verdad == True:
    numero = int(input("ingrese un numero entero: "))
    sumatoria = sumatoria + numero
    if numero == 0:
        valor_verdad = False
print("Total sumados es: ",sumatoria)

#5- Crea un juego en el que el usuario deba adivinar un numero aleatorio (0-9).
# Al final, el programa debe mostrar cuantos intentos fueron necesarios para acertar el numero. 

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

#6- Desarrolla un programa que imprima en pantalla todos los numeros pares comprendidos entre (0-100), en orden decreciente.

for i in range(100,0,-1):
    if i % 2 == 0:
        print(i)

#7- Crea un programa que calcule la suma de todos los numeros comprendidos entre 0 y un numero entero positivo indicado por el usuario

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

#8- Escribir un programa que permita al usuario ingresar 100 numeros enteros. Indicar: 
# -numeros pares 
# -numeros impares 
# -numeros negativos 
# -numeros positivos

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

#9- Elabora un programa que permita al usuario ingresar 100 numeros enteros y luego calcule la media de esos valores.

media: int = 0
promedio: float = 0
for i in range(1, 101):
    numero = int(input(f"ingrese el numero {i}: "))
    media = media + numero
promedio = media / i
print(f"El promedio de los {i} numeros es: {promedio}")

#10- Escriba un programa que invierta el orden de los digitos de un numero ingresado por el usuario.

numero = int(input("ingrese un numero: "))
invertido = 0
numero_cambiado = numero
while numero_cambiado > 0:
    ultimo_digito = numero_cambiado % 10
    invertido = (invertido * 10) + ultimo_digito
    numero_cambiado = int(numero_cambiado / 10)
print(f"La inversa del numero {numero} es: {invertido}")