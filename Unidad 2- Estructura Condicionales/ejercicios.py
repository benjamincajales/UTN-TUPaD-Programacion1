#alumno: Benjamin Cajales
#TP 3

#ejercicio 1

edad = int(input("ingrese la edad: "))
if (edad > 18):
    print("Es mayor de edad.")

#ejercicio 2

nota = int(input("ingrese su nota: "))
if (nota >= 6):
    print("Aprobado.")
else:
    print("Desaprobado.")

#ejercicio 3

numero = int(input("ingrese un numero par: "))
if numero % 2 != True:
    print("El numero es par.")
else:
    print("El numero no es par.")

#ejercicio 4

edad = int(input("ingrese su edad: "))
if (edad < 12):
    print("Usted es un niño/a.")
elif (edad >=12 and edad < 18):
    print("Usted es un adolecente.")
elif (edad >= 18 and edad < 30):
    print("Usted es un adulto/a joven.")
else:
    print("Usted es un Adulto/a.")

#ejercicio 5

contraseña = input("ingrese una contraseña: ")
print(len(contraseña))
if (len(contraseña) >= 8 and len(contraseña)<=14 != True):
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#ejercicio 6

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

#ejercicio 7

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

#ejercicio 8

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

#ejercicio 9

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

#ejercicio 10

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