#alumno: Benjamin Cajales

#ejercicio 1

print("Hola Mundo!")

#ejercicio 2

nombre = input("ingrese su nombre: ")
print(f"Hola {nombre}!")

#ejercicio 3

nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
edad = int(input("ingrese su edad: "))
lugar_residencia = input("ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}.")

#ejercicio 4

radio = float(input("ingresa el radio de un circulo: "))
area = 3.14 * (radio**2)
perimetro = 2 * 3.14 * radio
print(f"El radio es {radio}, su area es {area} y su perimetro es {perimetro}.")

#ejercicio 5

segundos = int(input("ingresa los segundos: "))
hora = segundos/3600
print(f"{segundos} segundos = {hora} horas.")

#ejercicio 6

valor = int(input("ingrese un numero para mostrar su tabla: "))
print(f"{valor} x 1 = ", valor * 1)
print(f"{valor} x 2 = ", valor * 2)
print(f"{valor} x 3 = ", valor * 3)
print(f"{valor} x 4 = ", valor * 4)
print(f"{valor} x 5 = ", valor * 5)
print(f"{valor} x 6 = ", valor * 6)
print(f"{valor} x 7 = ", valor * 7)
print(f"{valor} x 8 = ", valor * 8)
print(f"{valor} x 9 = ", valor * 9)
print(f"{valor} x 10 = ", valor * 10)

#ejercicio 7

num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))

print(f"La suma de los numeros {num1} y {num2} es: ",num1 + num2)
print(f"La resta de los numeros {num1} y {num2} es: ",num1 - num2)
print(f"El producto de los numeros {num1} y {num2} es: ",num1 * num2)
print(f"La division de los numeros {num1} y {num2} es: ",num1 / num2)

#ejercicio 8

altura = float(input("ingresa la altura (m): "))
peso = float(input("ingresa el peso (kg): "))
indice_corporal = peso / (altura**2)
print("El indice de masa corporal es: ",indice_corporal)

#ejercicio 9

celsius = float(input("ingrese una temperatura (celsius): "))
fahrenheit = (9/5) * celsius + 32
print("La temperatura es: ",fahrenheit)

#ejercicio 10

num1 = int(input("ingrese el primer numero: ")) 
num2 = int(input("ingrese el segundo numero: "))
num3 = int(input("ingrese el tercer numero: "))
promedio = (num1 + num2 + num3) / 3
print("El promedio de los 3 numeros es: ", promedio)