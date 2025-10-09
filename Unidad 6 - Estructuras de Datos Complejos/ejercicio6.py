#alumno: Benjamin Cajales
#TP6

#ejercicio 1

'''
Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
'''
precios_frutas: dict = {'Banana': 1200, 'Anana':2500,'Melon':3000,'Uva':1450}
print(precios_frutas)
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(precios_frutas)

#ejercicio 2

'''
Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800
'''
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melon"] = 1800
print(precios_frutas)

#ejercicio 3

'''
Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios.
'''
lista_claves: list = list(precios_frutas.keys())
print(lista_claves)

#ejercicio 4
'''
Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
'''
def es_numero_positivo(num):
    if num.isdigit():
        #digito entero
        num = int(num)
        return num

def cargar_numeros_telefonicos():
    #1 cargar 5 contactos con su nombre (clave) y numero 
    print("Cargar numeros telefonicos")
    for i in range(5):
        #---keys---
        clave = input(f"ingrese el nuevo contacto telefonico {i+1}: ")
        #---values---
        while True:
            valor = input(f"ingrese el numero telefonico de {clave.capitalize()}: ")
            #comprobacion
            valor = es_numero_positivo(valor)
            try:
                if valor == int(valor):
                    #agregamos el nombre del contacto (clave) y numero telefonico (valor)
                    numeros_telefonicos[clave.capitalize()] = valor
                    break
            except:
                print("numero invalido.")
        print(" ")

def consultar_numero_telefonico(busqueda_nombre):
    if busqueda_nombre in numeros_telefonicos:
        print(f"El numero telefonico del contacto {busqueda_nombre} es: {numeros_telefonicos[busqueda_nombre]}")
    else:
        print("El numero telefonico que menciono no existe")

numeros_telefonicos = {}

opcion: str = " "
while True: 
    print("--Menu--")
    print("0- agregar numero")
    print("1- consultar contacto")
    print("2- salir")
    opcion: str = input("ingrese una opcion: ")
    opcion = opcion.strip()
    opcion = es_numero_positivo(opcion)
    if opcion == 0:
        #0- cargamos numeros al diccionario (contactos)
        if not(numeros_telefonicos):
            cargar_numeros_telefonicos()
        else:
            print("numeros telefonicos cargados.")
    elif opcion == 1:
        #1- pedimos un nombre y mostramos el numero asociado (si existe)
        if not(numeros_telefonicos):
            print("numeros telefonicos no cargados")
        else:
            print("--Consultar numero telefonico--")
            busqueda_nombre = input("ingrese el nombre del contacto: ")
            busqueda_nombre = busqueda_nombre.capitalize().strip()
            consultar_numero_telefonico(busqueda_nombre)
    elif opcion == 2:
        #salir del bucle
        print("Salio exitosamente.")
        break
    else:
        print("Opcion no valida.")
    print(" ")

#ejercicio 5
'''
Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.
'''
#---solicitamos la frase---

frase: str = input("ingrese una frase: ")
#separamos la frase por espacios
lista: list = list(frase.split())

#---creamos set---
set_frase: set = set(lista)
print("set: ",set_frase)

#---creamos diccionario---

#trasformamos el set en lista
lista_set: list = list(set_frase)
diccionario_frase: dict = {}

#rellenamos el diccionario
for i in range(len(lista_set)):
    diccionario_frase[lista_set[i]] = lista.count(lista_set[i])
print("diccionario: ",diccionario_frase)

#ejercicio 6
'''
Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno
'''
def verificacion_notas():
    #comprobacion 
    comprobacion: bool = False
    nota: int = 0
    #notas
    nota = input("ingrese la nota [1-10]: ")
    while comprobacion == False:
        if nota.isdigit():
            nota = int(nota)
            if nota <= 0 or nota > 10:
                nota = input("Nota invalida, pruebe una nueva nota: ")
            else:
                return nota
                comprobacion = True
        else:
            nota = input("Nota invalida, pruebe una nueva nota: ")

def promedio_notas(tupla):
    promedio: float = 0
    for i in range(3):
        promedio = promedio + tupla[i]
    promedio_notas_alumnos.append(promedio/3)

diccionario_notas:dict = {}
promedio_notas_alumnos:list = []
#ingresamos los nombre de los 3 alumnos
for i in range(3):
    #notas
    nota_1 = 0
    nota_2 = 0
    nota_3 = 0
    alumno = input(f"ingrese el nombre del alumno {i+1}: ")
    alumno = alumno.capitalize()
    
    #ingresamos las notas 
    print("Nota 1: ", end="")
    nota_1 = verificacion_notas()
    print("Nota 2: ", end="")
    nota_2 = verificacion_notas()
    print("Nota 3: ", end="")
    nota_3 = verificacion_notas()

    #inicializamos una tupla
    tupla_notas = (nota_1,nota_2,nota_3)
    #mostramos promedio de las 3 notas
    promedio_notas(tupla_notas)
    
    #insertamos a la lista
    diccionario_notas[alumno] = tupla_notas
    print(" ")

print("Notas: ")
i = 0
for clave, valor in diccionario_notas.items():
    print(f"Alumno {clave}, Notas: {valor}, Promedio de notas: {promedio_notas_alumnos[i]}")
    i += 1

#ejercicio 7
'''
Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
'''

set1: set = {1,3,4,5,4,10,2}
set2: set = {1,25,14,7,2,6}
print("Notas Aprobados: ")
print("Parcial 1: ",set1)
print("Parcial 2: ",set2)
#mostramos los que aprobaron ambos parciales
ambos_parciales: set = set1 & set2
print("Los alumnos que aprobaron ambos parciales son: ",ambos_parciales)
#mostramos los que aprobaron solo uno de los dos
solo_uno_de_los_dos: set = set1 ^ set2
print("Los alumnos que aprobaron solo uno de los dos: ",solo_uno_de_los_dos)
#mostramos todos los estudiantes que aprobaron al menos un parcial
al_menos_un_parcial = ambos_parciales | solo_uno_de_los_dos
print("Los estudiantes que aprobaron al menos un parcial: ",al_menos_un_parcial)

#ejercicio 8
'''
Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.
'''
def es_numero_positivo(num):
    if num.isdigit():
        num = int(num)
        return num
    else:
        print("Digito no valido.")

def consultar_producto(producto):
        if producto in inventario:
            print(" ")
            print(
                f"El producto {producto} tiene {inventario[producto]} stocks"
                )
        else:
            print("El producto no se encuentra. ")

def agregar_stock(producto):
    if producto in inventario:
        #ingresamos la cantidad de stock que queremos agregar al producto existente
        cantidad_stock: int = input("ingrese la cantidad de stock quiere agregar al producto: ")
        cantidad_stock = es_numero_positivo(cantidad_stock)

        #try-except para comprobar que muestre solo cuando el valor ingresado sea solo digito
        try:
            if cantidad_stock == int(cantidad_stock):
                inventario[producto] += cantidad_stock
                print("Se agrego exitosamente.")
        except:
            pass
    else:
        print("El producto no se encuentra.")

def agregar_producto(producto):
    if not(producto in inventario):
        nuevo_stock = input("ingrese la cantidad de stock del nuevo producto: ")
        nuevo_stock = es_numero_positivo(nuevo_stock)
        #try-except para solo ingresar un numero entero positivo
        try:
            if nuevo_stock == int(nuevo_stock):
                inventario[producto] = nuevo_stock
                print("Se agrego exitosamente el nuevo producto.")
        except:
            pass
    else:
        print("El producto se encuentra.")

#diccionario
#keys: nombres de productos, value: stock
inventario = {
    "Computadora": 15,
    "Mouse": 50,
    "Teclado": 25,
    "Monitor": 8
}

opcion: int = 0

while True:
    print(inventario)
    print("--Menu--")
    print("0- consultar producto")
    print("1- agregar stock a un producto existente")
    print("2- agregar un nuevo producto")
    print("3- Salir")
    opcion: str = input("ingrese una de las opciones: ")
    opcion = es_numero_positivo(opcion)
    
    if opcion == 0:
        #opcion 0- consultar stock
        print(" ")
        print("--Consultar producto--")
        producto = input("ingrese el nombre del producto: ")
        producto = producto.capitalize().strip()
        consultar_producto(producto)
        print(" ")
    
    elif opcion == 1:
        #opcion 1 - agregar un stock
        print(" ")
        print("--Agregar stock--")
        producto = input("ingrese el nombre del producto: ")
        producto = producto.capitalize().strip()
        agregar_stock(producto)
        print(" ")
    
    elif opcion == 2:
        #opcion 2 - agregar un nuevo producto
        print(" ")
        print("--Agregar un nuevo producto--")
        nuevo_producto = input("ingrese el nombre del nuevo producto: ")
        nuevo_producto = nuevo_producto.capitalize().strip()
        agregar_producto(nuevo_producto)
        print(" ")
    
    elif opcion == 3:
        #opcion 3 - salida
        print("Salio exitosamente")
        break
        
    else:
        print("La opcion ingresada no es valida.")
    print(" ")

#ejercicio 9
'''
Creá una agenda donde las claves sean tuplas de (dia, hora) y los valores sean eventos
Permití consultar qué actividad hay en cierto día y hora.
'''
def actividades_cantidad():
    cantidad = input("ingrese la cantidad de actividades que quiere agregar: ")
    cantidad = es_numero(cantidad)
    return cantidad

def dias (i):
    while True:
        print(" ")
        print("Seleccione semana: ")
        print("0- Lunes")
        print("1- Martes")
        print("2- Miercoles")
        print("3- Jueves")
        print("4- Viernes")
        print("5- Sabado")
        print("6- Domingo")
        seleccionar_dia = input(f"ingrese el dia {i+1}: ")
        seleccionar_dia = es_numero(seleccionar_dia)
        if seleccionar_dia > 6:
            print(" ")
            print("opcion invalida, ingrese una nueva opcion")
        else:
            if seleccionar_dia == 0:
                return "Lunes"
            elif seleccionar_dia == 1:
                return "Martes"
            elif seleccionar_dia == 2:
                return "Miercoles"
            elif seleccionar_dia == 3:
                return "Jueves"
            elif seleccionar_dia == 4:
                return "Viernes"
            elif seleccionar_dia == 5:
                return "Sabado"
            elif seleccionar_dia == 6:
                return "Domingo"
            
            print("opcion ingresada correctamente")
            break 

def horas(i):
    while True:
        print(f"Hora y minutos del dia {i+1}")
        #hora
        hora = input("ingrese la hora: ")
        hora = es_numero(hora)
        #minutos
        minutos = input("ingrese los minutos: ")
        minutos = es_numero(minutos)
        if hora > 23 or minutos > 59:
            print("Hora o minutos incorrectos, ingrese nuevamente una nueva hora")
        else:
            print("Hora y minutos insertados exitosamente")
            return (f"{hora}:{minutos}")
            break

def actividades(i):
    actividad = input(f"ingrese la actividad que va hacer el dia {i+1}: ")
    return actividad

def es_numero(num):
    while True:
        if num.isdigit():
            num = int(num)
            if num >= 0:
                return num
                break
        else:
            num = input("numero incorrecto o negativo, ingrese un nuevo valor: ")

agenda = {}
cantidad = actividades_cantidad()
print(" ")
for i in range(cantidad):
    print(f"Dia {i+1}")
    #dia
    dia = dias(i)
    print(" ")
    #hora
    hora = horas(i)
    print(" ")
    #actividad del dia
    actividad = actividades(i)
    agenda[(dia,hora)] = actividad

print(" ")
print("Agenda:")
for clave, valor in agenda.items():
    print(f"{clave}, actividad: {valor}")

#ejercicio 10