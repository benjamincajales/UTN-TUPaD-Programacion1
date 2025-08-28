#alumno: Benjamin Cajales
#TP 2

#1- Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#debera mostrar un mensaje en pantall que diga "Es mayor de edad".

edad = int(input("ingrese la edad: "))
if (edad > 18):
    print("Es mayor de edad.")

#2- Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6,
#debera mostrar por pantalla un mensaje que diga "Aprobado"; en caso contrario debera mostrar el mensaje "Desaprobado"

nota = int(input("ingrese su nota: "))
if (nota >= 6):
    print("Aprobado.")
else:
    print("Desaprobado.")

#3- Escribir un programa que permita ingresar solo numeros pares. Si el usuario ingresa un numero par,
#imprimir en pantalla el mensaje "Ha ingresado un numero par", en caso contrario, imprimir por pantalla 
# "Por favor, ingrese un numero par"

numero = int(input("ingrese un numero par: "))
if numero % 2 != True:
    print("El numero es par.")
else:
    print("El numero no es par.")

#4- Escribir un programa que solicite al usuario su edad e imprima por pantalla a cual de las siguientes 
#categorias pertenece:
#niño/a:  < 12 años, adolescente: >= 12 años and < 18 años, adulto/a joven: >= 18 años and < 30 años, adulto/a: >= 30 años

edad = int(input("ingrese su edad: "))
if (edad < 12):
    print("Usted es un niño/a.")
elif (edad >=12 and edad < 18):
    print("Usted es un adolecente.")
elif (edad >= 18 and edad < 30):
    print("Usted es un adulto/a joven.")
else:
    print("Usted es un Adulto/a.")

#5- Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14).
#Si el usuarui ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"
#, en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".

contraseña = input("ingrese una contraseña: ")
print(len(contraseña))
if (len(contraseña) >= 8 and len(contraseña)<=14 != True):
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#6- importa la libreria statistics y calcula la moda, mediana y la media de dichos numeros.
# Generados en una lista de 100 elementos de manera random, importar la libreria random.
# -sesgo positivo o a la derecha: media > mediana and mediana > moda
# -sesgo negativo o a la izquierda: media < mediana and mediana < moda
# -sin sesgo: media == mediana and mediana == moda

from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if (media > mediana and mediana > moda):
    print("Sesgo positivo o a la derecha")
elif(media < mediana and mediana < moda):
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo")

#7- Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal,
# añadir un signo de exclamacion al final e imprimir el string resultante por pantalla; en caso contrario,
# dejar el string tal cual lo ingreso el usuario e imprimirlo por pantalla.

frase = input("ingrese una frase: ")
long = len(frase)
if (frase[long-1] == "a"):
    print(frase + "!")
elif (frase[long-1] == "e"):
    print(frase + "!")
elif (frase[long-1] == "i"):
    print(frase + "!")
elif (frase[long-1] == "o"):
    print(frase + "!")
elif (frase[long-1] == "u"):
    print(frase + "!")
else:
    print(frase)

#8- Solicite al usuario que ingrese su nombre y el numero 1,2 o 3 dependiendo de la opcion:
# -1 Si quiere su nombre en mayusculas.
# -2 Si quiere su nombre en minusculas.
# -3 Si quiere su nombre con la primera letra mayuscula.

nombre = input("ingrese su nombre: ")
digito = int(input("ingrese un numero (1,2,3): "))
if (digito == 1):
    print(nombre.upper())
elif (digito == 2):
    print(nombre.lower())
elif (digito == 3):
    print(nombre.capitalize())
else:
    print("ha ingresado un numero incorrecto.")

#9- Escribir un programa que pida al usuario la magnitud de un terremoto. Clasifique la magnitud en una de las siguientes categorias:
# < 3: "Muy leve"
# >= 3 and < 4: "Leve"
# >= 4 and < 5: "Moderado"
# >= 5 and < 6: "Fuerte"
# >= 6 y < 7: "Muy fuerte"
# >= 7: "Extremo"

magnitud = int(input("ingrese la magnitud del terremoto: "))
if (magnitud < 3 and magnitud > 0):
    print("Muy leve.")
elif (magnitud >= 3 and magnitud < 4):
    print("Leve.")
elif (magnitud >= 4 and magnitud < 5):
    print("Fuerte.")
elif (magnitud >=5 and magnitud < 7):
    print("Muy fuerte.")
elif (magnitud >= 7):
    print("Extremo.")
else:
    print("La magnitud ingresada no es valida.")

#10- Utilizando la informacion aportada sobre las estaciones del año.
# Periodo del año   |   Estacion (hemisferio Norte)     |    Estacion (hemisferio Sur).
# 21/12 hasta 20/3  |           Invierno                |    Verano
# 21/3 hasta 20/6   |           Primavera               |    Otoño
# 21/6 hasta 20/9   |           Verano                  |    Invierno
# 21/9 hasta 20/12  |           Otoño                   |    Primavera
# Escribir un programa que pregunte al usuario en cual hemisferio se encuentra, mes y dia;
# mostrar por salida en que estacion del año se encuentra.

hemisferio = input("ingrese el hemisferio (norte/sur): ")
hemisferio = hemisferio.upper()
mes = input("ingrese el mes (enero,febrero,...): ")
mes = mes.lower()
dia = int(input("ingrese el dia/fecha (1,2,3,...): "))
#enero,febrero,marzo*,abril,mayo,junio*,julio,agosto,septiembre*,octubre,noviembre,diciembre*
print(f"Se encuentra en el hemisferio {hemisferio}, en el mes {mes} y dia {dia}: ")
#cambiamos la variable mes para trabajar mejor
if(hemisferio == "NORTE"):
    hemisferio = "n"
else:
    hemisferio = "s"
#Hemisferio Norte
if (hemisferio == "n"):
    #Meses (norte)
    if (mes == "enero"):
        print("Se encuentra en invierno.")
    elif (mes == "febrero"):
        print("Se encuentra en invierno.")
    elif (mes == "marzo"):
        if (dia >= 21):
            print("Se encuentra en primavera.")
        else:
            print("Se encuentra en invierno.")
    elif (mes == "abril"):
        print("Se encuentra en primavera.")
    elif (mes == "mayo"):
        print("Se encuentra en primavera.")
    elif (mes == "junio"):
        if (dia >= 21):
            print("Se encuentra en verano.")
        else:
            print("Se encuentra en primavera.")
    elif (mes == "julio"):
        print("Se encuentra en verano.")
    elif (mes == "agosto"):
        print("Se encuentra en verano.")
    elif (mes == "septiembre"):
        if(dia >= 21):
            print("Se encuentra en otoño.")
        else:
            print("Se encuentra en verano.")
    elif (mes == "octubre"):
        print("Se encuentra en otoño.")
    elif (mes == "noviembre"):
        print("Se encuentra en otoño.")
    elif (mes == "diciembre"):
        if(dia >= 21):
            print("Se encuentra en invierno.")
        else:
            print("Se encuentra en otoño.")
    else:
        print("No existe ese mes.")
elif (hemisferio == "s"):
    #Hemisferio Sur
    #Meses (sur)
    if (mes == "enero"):
        print("Se encuentra en verano.")
    elif (mes == "febrero"):
        print("Se encuentra en verano.")
    elif (mes == "marzo"):
        if (dia >= 21):
            print("Se encuentra en otoño.")
        else:
            print("Se encuentra en verano.")
    elif (mes == "abril"):
        print("Se encuentra en otoño.")
    elif (mes == "mayo"):
        print("Se encuentra en otoño.")
    elif (mes == "junio"):
        if (dia >= 21):
            print("Se encuentra en invierno.")
        else:
            print("Se encuentra en otoño.")
    elif (mes == "julio"):
        print("Se encuentra en invierno.")
    elif (mes == "agosto"):
        print("Se encuentra en invierno.")
    elif (mes == "septiembre"):
        if(dia >= 21):
            print("Se encuentra en primavera.")
        else:
            print("Se encuentra en invierno.")
    elif (mes == "octubre"):
        print("Se encuentra en primavera.")
    elif (mes == "noviembre"):
        print("Se encuentra en primavera.")
    elif (mes == "diciembre"):
        if(dia >= 21):
            print("Se encuentra en verano.")
        else:
            print("Se encuentra en primavera.")
    else:
        print("No existe ese mes.")
else:
    print("Hemisferio no valido.")