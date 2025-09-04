#Mini Conecta-3:
#Objetivos: como Conecta-4 pero en 4x4 y alineando 3
#Pistas:-Tablero 4x4 con "." 
#       -ingresar columnas (0-3). La ficha "cae" desde abajo (busca la primera celda "." de abajo hacia abajo) 
#       -chequea 3 en linea (horiz, vert, diag.) con bucles simples.
#       -sin def y sin comprehensions 
#       -extra: contar jugadas maximas (16) para empatar

#nota: falta agregar las verificaciones de los 3 en raya, para cada caso

print("---Conecta-3---")

print("Ingrese la ficha del jugador 1:")
print("ficha: r")#r = rojo
print("ficha: a")#a = amarrillo
jugador1 = input("Jugador 1: ")

#los valores ingresados seran en minuscula
jugador1 = jugador1.lower()

#bucle para determinar que no ingrese otros elementos que no sean x ó o
while jugador1 != "r" and jugador1 != "a":
    jugador1 = input("error, ingrese una ficha valida: ")
    jugador1 = jugador1.lower()

#agregamos las fichas de cada jugador
if jugador1 == "r":
    jugador2 = "a"
else:
    jugador2 = "r"

#inicializamos el tablero
tablero = [
    [".",".",".","."],
    [".",".",".","."],
    [".",".",".","."],
    [".",".",".","."]
]

#inicializamos jugadas
jugadas = 1

#mostramos tablero
print("")
print("--Tablero--")
print("     0    1    2    3")
print(f"0  {tablero[0]}")
print(f"1  {tablero[1]}")
print(f"2  {tablero[2]}")
print(f"3  {tablero[3]}")
print("")
print("--------------------")

#distintos casos de comprobacion
comprobacion_caso1 = False # comprobamos si las filas forman 3 en raya
comprobacion_caso2 = False # comprobamos si las columnas forman 3 en raya
comprobacion_caso3 = False # comprobamos si las columnas forman 3 en raya

#bucle para iterar entre las jugadas
while jugadas <= 16:
    
    #variable para comprobar si una columna indicada esta lleno o no
    esta_lleno_columna = False
    #variable itera entre filas
    contador_fila = 3
    #variable para determinar que ya se ocupo un lugar
    lugar_ocupado = False

    #muestra las jugadas y el jugador
    if jugadas % 2 != 0:
        print(f"Jugada {jugadas} -  jugador 1")
        
        while esta_lleno_columna == False:
            
            #columna
            columna = int(input("ingrese una columna: "))

            while columna < 0 or columna >3:
                print("indice fuera de rango, pruebe con otro indice")
                columna = int(input("columna: "))

            #comprobamos que no este lleno
            #variable para contar los espacios que estan ocupados en la columna indicada
            contador = 0
            for fila in range(4):
                if tablero[fila][columna] == "r" or tablero[fila][columna] == "a":
                    contador += 1
            
            #condicional para indicar al usuario si esta lleno esa columna
            
            if contador == 4 :
                print("columna llena, pruebe con otra columna")
                esta_lleno_columna = False
            else:
                
                #buscamos un elemento vacio
                while lugar_ocupado == False:
                    if tablero[contador_fila][columna] == ".":
                        tablero[contador_fila][columna] = jugador1
                        lugar_ocupado = True
                    esta_lleno_columna = True
                    contador_fila -=1
    else:
        print(f"Jugada {jugadas} - jugador 2")
        
        #columna
        columna = int(input("ingrese una columna: "))
        while columna < 0 or columna >3:
            print("indice fuera de rango, pruebe con otro indice")
            columna = int(input("columna: "))
        
        #comprobamos que no este lleno
        #variable para contar los espacios que estan ocupados en la columna indicada
        contador = 0
        for fila in range(4):
            if tablero[fila][columna] == "r" or tablero[fila][columna] == "a":
                contador += 1
        
        #condicional para indicar al usuario si esta lleno esa columna
        
        if contador == 4 :
            print("columna llena, pruebe con otra columna")
            esta_lleno_columna = False
        else:
            
            #buscamos un elemento vacio
            while lugar_ocupado == False:
                if tablero[contador_fila][columna] == ".":
                    tablero[contador_fila][columna] = jugador2
                    lugar_ocupado = True
                esta_lleno_columna = True
                contador_fila -=1
    
    #verificacion para comprobar si las fichas son iguales

    #caso 1: igual fichas en filas

    #1- iteramos los primeros 3 elementos (0-2)
    #2- iteramos los ultimos 3 elementos (1-3)

    #caso 2: igual fichas en columnas

    #1- iteramos las primeras 3 columnas (0-2)
    #2- iteramos las ultimas 3 columnas (1-3) 

    #caso 3: igual fichas en diagonal

    #diagonales principales
    #1- [[3.0],[2,1],[1,2]] 
    #2- [[2,1],[1,2],[0,3]]
    #diagonales secundaria
    #3- [[2,0],[1,1],[0,2]] 
    #4- [[3,0],[2,2],[1,3]]

    #mostramos tablero
    print("")
    print("--Tablero--")
    print("     0    1    2    3")
    print(f"0  {tablero[0]}")
    print(f"1  {tablero[1]}")
    print(f"2  {tablero[2]}")
    print(f"3  {tablero[3]}")
    print("")
    print("--------------------")

    #incrementamos las jugadas
    jugadas +=1



if jugadas > 16:
    print("Perdio!")