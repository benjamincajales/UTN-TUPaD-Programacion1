#alumno: Benjamin Cajales
#TP 4

#1- Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

lista_multiplo_4 = []

for numero in range(101):
    if numero % 4 == 0:
        lista_multiplo_4.append(numero)

print(lista_multiplo_4)

#2- Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 

lista = ["manzana", "naranja","cereza","banana", "sandia"]

print(f"mostramos por indice positivo: {lista[3]}")
print(f"mostramos por indice negativo: {lista[-2]}")

#3- Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. 

lista = []

lista.append("tres")
lista.append("palabras")
lista.append("con")

print(lista)

#4- Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. 
# animales = ["perro","gato","conejo","pez"]

animales = ['perro', 'gato', 'conejo', 'pez']

print("lista original: ",animales)
animales[1] = 'loro'
animales[-1] = 'oso'
print("Lista modificada: ",animales)

#5- Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)

#Conclusion: el programa remueve el maximo elemento que posee la lista y luego lo imprime por pantalla

#6- Crear una lista con números del 10 al 30 (incluído), 
# haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

lista = []

lista = list(range(10,31,5))

print(lista[0])
print(lista[1])

#7-  Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” 
# por dos nuevos valores cualesquiera. 
# autos = ['sedan','polo','suran','gol']

auto = ['sedan','polo','suran','gol']
print(f"la lista original: {auto}")
auto[1] = 100
auto[2] = 1000
print(f"la lista modificada: {auto}")

#8- Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente.
# Imprimir la lista resultante por pantalla.

doble = []

doble.append(5*2)
doble.append(10*2)
doble.append(15*2)

print(doble)

#9- Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes: 
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras = [
    ["pan","leche"],
    ["arroz","fideos","salsa"],
    ["agua"]
    ]
print(f"Lista original: {compras}")
#a) agregamos "jugo" a la tercer lista
compras[2].append("jugo")
#b) reemplazamos "fideos" por "tallarines" en la segunda lista
compras[1][1] = "tallarines"
#c) eliminamos "pan" de la primer lista
compras[0].remove("pan")
print(f"Lista modificada: {compras}")

#Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#- Posición lista_anidada[0]: 15
#- Posición lista_anidada[1]: True
#- Posición lista_anidada[2][0]: 25.5
#- Posición lista_anidada[2][1]: 57.9
#- Posición lista_anidada[2][2]: 30.6
#- Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.

lista_anidada = [15,True,[25.5,57.9,30.6],False]

print(lista_anidada)