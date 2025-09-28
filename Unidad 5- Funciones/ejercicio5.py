#alumno: Benjamin Cajales
#TP1

#ejercicio 1

'''Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.
'''

def imprimir_hola_mundo():
    print("Hola Mundo!")

#llamamos al subproceso
imprimir_hola_mundo()

#ejercicio 2

'''
Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. 
Llamar a esta función desde el programa principal solicitando el nombre al usuario.
'''

def saludar_usuario(nombre):
    print(f"Hola {nombre} un gusto en conocerte!")

#nombre
nombre: str = input("ingrese su nombre: ")

#llamamos al subproceso
saludar_usuario(nombre)

#ejercicio 3

'''
Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
Pedir los datos al usuario y llamar a esta función con los valores ingresados.
'''

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre.capitalize()} {apellido.capitalize()}, tengo {edad} años y vivo en {residencia.capitalize()}")

#nombre
nombre = input("ingrese su nombre: ")
#apellido
apellido = input("ingrese su apellido: ")
#edad
edad = int(input("ingrese su edad: "))

#condicion para que la edad no sea menor a 0
while edad <= 0:
    edad = int(input("edad invalida, inserte otro valor: "))
#residencia
residencia = input("ingrese su residencia: ")

#llamamos al subproceso
informacion_personal(nombre, apellido, edad, residencia)

#ejercicio 4

'''
Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y
devuelva el área del círculo. 
calcular_perimetro_circulo(radio) que reciba el radio como parámetro y 
devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones
para mostrar los resultados.
'''
from math import pi

def calcular_area_circulo(radio):
    area_circulo: float = 0
    area_circulo = pi * (radio**2)
    return area_circulo

def calcular_perimetro_circulo(radio):
    perimetro_circulo: float = 0
    perimetro_circulo = 2 * pi * radio
    return perimetro_circulo 

#radio
radio: float = float(input("ingrese el radio del circulo: "))

#condicion para determinar que el radio no sea menor o igual a 0
while radio <= 0:
    radio = float(input("radio invalido, ingrese con un radio positivo: ")) 

#llamamos a las funciones
area: float = calcular_area_circulo(radio)
perimetro: float = calcular_perimetro_circulo(radio)

print(f"area: {area}, perimetro: {perimetro}")

#ejercicio 5

'''
Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
'''

def segundos_a_horas(segundos):
    hora: float = 0
    hora = segundos / 3600
    return hora

#segundos
segundos: int = int(input("ingrese los segundos que quiere convertir: "))

#condicion para determinar que los segundos no sean negativos
while segundos < 0:
    segundos = int(input("segundos invalido, ingrese un nuevo valor: "))

#llamamos a la funcion
hora = segundos_a_horas(segundos)

print(f"{segundos}s en hora es: {hora} hs")

#ejercicio 6

'''
Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función.
'''

def tabla_multiplicar(num):
    for i in range(10):
        resultado_multiplicar.append( (i+1) *num)
    return resultado_multiplicar


numero: int = int(input("ingrese un numero para la tabla de multiplicar: "))

#condicion para determinar que no elija menor o igual a 0
while numero <= 0:
    numero = int(input("numero invalido, ingrese un nuevo numero: "))

#llamamos a la funcion
resultado_multiplicar = list()
resultado_multiplicar = tabla_multiplicar(numero)

#mostramos el producto del numero ingresado
print(f"Tabla de multiplicar {numero}")
for i in range(1,11):
    print(f"{numero} x {i} = {resultado_multiplicar[i-1]}")

#ejercicio 7

'''
Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, 
restarlos, multiplicarlos y dividirlos. 
Mostrar los resultados de forma clara.
'''
def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    producto = a * b
    if b != 0:
        division = a / b
    else:
        division = "No es posible"
    return (suma,resta,producto,division)

#ingresamos los numeros
num1: int = int(input("ingrese el primer numero: "))
num2: int = int(input("ingrese el segundo numero: "))

#llamamos a la funcion
resultado_operaciones: tuple = operaciones_basicas(num1, num2)

#mostramos los resultados
print(" ")
print(f"Numeros: {num1}, {num2}")
print("Operaciones: ")
for i in range(4):
    if i == 0:
        print(f"La suma es: {resultado_operaciones[0]}")
    elif i == 1:
        print(f"La resta es: {resultado_operaciones[1]}")
    elif i == 2:
        print(f"La multiplicacion es: {resultado_operaciones[2]}")
    elif i == 3:
        print(f"La division es: {resultado_operaciones[3]}")

#ejercicio 8

'''
Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la 
función para mostrar el resultado con dos decimales.
'''

def calcular_imc(peso, altura):
    #imc = peso(kg)/ altura(m)²
    imc = peso / (altura**2)
    return imc


print("Indice de masa corporal (IMC)")
#peso
peso: float = float(input("ingrese el peso (kg): "))

#condicion para que no ingrese un numero menor o igual a 0
while peso <= 0:
    peso = int(input("peso incorrecto, ingrese otro peso: "))

#altura
altura = float(input("ingrese la altura (mt): "))

#condicion para que no ingrese un numero menor o igual a 0
while altura <= 0:
    altura = float("altura incorrecta, ingrese otra altura: ")

#llamamos a la funcion
imc: float = calcular_imc(peso, altura)

#mostramos el resultado final
print("El IMC es: ",round(imc,2))

#ejercicio 9

'''
Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
'''

def celsius_a_fahrenheit(celsius):
    #F° = (C° * (9 / 5))+32
    fahrenheit = (celsius * (9/5)) + 32
    return fahrenheit

print("temperatura celsius en fahrenheit")

#celsius
celsius: float = float(input("ingrese la temperatura en celsius: "))

#llamamos a la funcion
fahrenheit: float = celsius_a_fahrenheit(celsius)

#mostramos el resultado
print(f"La temperatura en celsius {celsius} en fahrenheit es: {fahrenheit}")

#ejercicio 10

'''
Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
'''

def calcular_promedio(a, b, c):
    promedio: float = a + b + c
    promedio: float = promedio / 3
    return promedio

print("El promedio de 3 numeros")
#numero 1
num1: int = int(input("ingresa el primer numero: "))
#numero 2
num2: int = int(input("ingresa el segundo numero: "))
#numero 3
num3: int = int(input("ingresa el tercer numero: "))

#llamamos a la funcion
promedio: float = calcular_promedio(num1,num2,num3)

#mostramos el resultado
print("El promedio de los 3 numeros es: ",promedio)
