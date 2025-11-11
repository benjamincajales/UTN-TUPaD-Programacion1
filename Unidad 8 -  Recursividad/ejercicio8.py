'''
1. Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario
'''
def es_numero_positivo(mensaje):
    while True:
        numero = input(mensaje)
        #si es un numero positivo ingresa aqui
        if numero.isdigit():
            numero = int(numero)
            #si el numero es menor o igual a 1, entonces muestra mensaje y regresa otra vez
            if numero < 1:
                print ("El numero debe ser mayor o igual a 1")
                continue
            else:
                #el numero es admitido y mayor a 1
                return numero
        #muestra mensaje que no es un numero positivo
        print("numero no admitido")

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)

def main():
    maximo = es_numero_positivo("ingrese un numero positivo y mayor a 1: ")
    minimo = 1
    #recorremos las iteraciones
    for minimo in range(1,maximo+1):
        print(f"El factorial {minimo} es: {factorial(minimo)}")

main()

'''
2. Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.
'''

def es_numero_positivo(mensaje):
    while True:
        numero = input(mensaje)
        #si es un numero positivo ingresa aqui
        if numero.isdigit():
            numero = int(numero)
            #si el numero es menor o igual a 1, entonces muestra mensaje y regresa otra vez
            if numero < 1:
                print ("El numero debe ser mayor o igual a 1")
                continue
            else:
                #el numero es admitido y mayor a 1
                return numero
        #muestra mensaje que no es un numero positivo
        print("numero no admitido")

def serie_fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return serie_fibonacci(num -1) + serie_fibonacci(num - 2)

def main():
    indice = es_numero_positivo("ingrese la posicion donde quiere efectuar la serie de Fibonacci: ")
    #recorremos los numeros
    print("Serie Fibonacci: ")
    for i in range(indice+1):
        print(f"{i}: {serie_fibonacci(i)}")

main()

'''
3. Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula n ^ m = n * n^(m -1). 
Prueba esta función en un algoritmo general.
'''
def es_numero_positivo(mensaje):
    while True:
        numero = input(mensaje)
        #si es un numero positivo ingresa aqui
        if numero.isdigit():
            numero = int(numero)
            #si el numero es menor o igual a 1, entonces muestra mensaje y regresa otra vez
            if numero < 1:
                print ("El numero debe ser mayor o igual a 1")
                continue
            else:
                #el numero es admitido y mayor a 1
                return numero
        #muestra mensaje que no es un numero positivo
        print("numero no admitido")

def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)

def main():
    exponente = es_numero_positivo("ingrese un exponente: ")
    base = es_numero_positivo("ingrese una base: ")
    resultado = potencia_recursiva(base,exponente)
    print("El resultado de la formula es: ",resultado)

main()

'''
4. Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
'''

def es_numero_positivo(mensaje):
    while True:
        numero = input(mensaje)
        #si es un numero positivo ingresa aqui
        if numero.isdigit():
            numero = int(numero)
            #si el numero es menor o igual a 1, entonces muestra mensaje y regresa otra vez
            if numero < 1:
                print ("El numero debe ser mayor o igual a 1")
                continue
            else:
                #el numero es admitido y mayor a 1
                return numero
        #muestra mensaje que no es un numero positivo
        print("numero no admitido")

def decimal_a_binario(num):
    if num < 2:
        return str(num)
    else:
        return decimal_a_binario(num // 2) + str(num % 2)

def main():
    numero = es_numero_positivo("ingrese un numero: ")
    print(f"Decimal {numero} | Binario: {decimal_a_binario(numero)}")

main()

'''
5. Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed().
'''
def palabra_modificada(palabra):
    return ''.join(palabra.lower().strip().split())

def es_palindromo(palabra):
    #modificamos la palabra para que este en minuscula y sin espacios
    palabra = palabra_modificada(palabra)
    #caso base, si la palabra tiene 0 o 1 caracter, es un polindromo
    if len(palabra) <= 1:
        return True
    #caso base, si es mayor a 1
    if palabra[0] != palabra[-1]:
        return False
    #paso recursivo
    return es_palindromo(palabra[1:-1])

def main():
    palabra = input("ingrese una palabra para determinar si es palindromo: ")

    if es_palindromo(palabra):
        print("La palabra es un palindromo")
    else:
        print("La palabra no es un palindromo")

main()

'''
6. Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
'''
def es_numero_positivo(mensaje):
    while True:
        numero = input(mensaje)
        #si es un numero positivo ingresa aqui
        if numero.isdigit():
            numero = int(numero)
            return numero
        #muestra mensaje que no es un numero positivo
        print("numero no admitido")

def suma_digitos(n):
    #caso base
    if n < 10:
        return n
    else:
        #obtenemos el ultimo digito
        ultimo_digito = n % 10
        #obtenemos el resto del numero
        resto = n // 10
        #retorno recursivo
        return ultimo_digito + suma_digitos(resto)

digito = suma_digitos(es_numero_positivo("ingrese un numero positivo y entero: "))

print("La suma de los digitos es: ",digito)

'''
7. Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.

Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
'''
def es_numero_positivo(mensaje):
    while True:
        numero = input(mensaje)
        #si es un numero positivo ingresa aqui
        if numero.isdigit():
            numero = int(numero)
            #si el numero es menor o igual a 1, entonces muestra mensaje y regresa otra vez
            if numero < 1:
                print ("El numero debe ser mayor o igual a 1")
                continue
            else:
                #el numero es admitido y mayor a 1
                return numero
        #muestra mensaje que no es un numero positivo
        print("numero no admitido")

def contar_bloques(n):
    #caso base
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

numero = contar_bloques(es_numero_positivo("ingrese un numero mayor a 0: "))

print("La suma de los numeros : ",numero)

'''
8. Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
'''
def es_numero_positivo(mensaje):
    while True:
        numero = input(mensaje)
        #si es un numero positivo ingresa aqui
        if numero.isdigit():
            numero = int(numero)
            return numero
        #muestra mensaje que no es un numero positivo
        print("numero no admitido")

def contar_digito(numero, digito):
    if numero < 10:
        if numero == digito:
            #retorna 1 si son iguales
            return 1
        else:
            #retorna 0, si son diferentes
            return 0
    else:
        #comparamos el ultimo digito
        ultimo_digito = numero % 10
        
        if ultimo_digito == digito:
            cuenta_actual = 1
        else:
            cuenta_actual = 0
        
        #obtenemos el resto del numero
        resto = numero // 10
        #recursividad
        return cuenta_actual + contar_digito(resto, digito)

numero = es_numero_positivo("ingrese un numero positivo: ")

digito = es_numero_positivo("ingrese un digito entre 0-9: ")

while True:
    if digito > 9:
        digito = es_numero_positivo("numero no admitido, pruebe nuevamente entre 0-9: ")
    else:
        break

repetidos = contar_digito(numero, digito)