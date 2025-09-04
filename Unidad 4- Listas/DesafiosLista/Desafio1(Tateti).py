#Tateti (3x3): 
#Objetivos: dos jugadores (x y o) marcan por turnos. Gana quien alinee 3. 
#Pide: fila y columna (0-2). Valida jugadas, muestra tablero, detecta ganador o empate.

print("---Ta-Te-Ti---")
print("Ingrese la ficha del jugador 1:")
print("ficha: x")
print("ficha: o")
jugador1 = input("Jugador 1: ")

#los valores ingresados seran en minuscula
jugador1 = jugador1.lower()

#bucle para determinar que no ingrese otros elementos que no sean x ó o
while jugador1 != "x" and jugador1 != "o":
    jugador1 = input("error, ingrese una ficha valida: ")
    jugador1 = jugador1.lower()

#agregamos las fichas de cada jugador
if jugador1 == "x":
    jugador2 = "o"
else:
    jugador2 = "x"

#Turnos, si el turno es impar mostrara al jugador 1 o sino al jugador 2
turnos = 1

#inicializamos tablero (3x3)
tablero = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
        ]

#Mostramos tablero
print("")
print("--Tablero--")
print("     0    1    2")
print(f"0  {tablero[0]}")
print(f"1  {tablero[1]}")
print(f"2  {tablero[2]}")

print("--------------------")

#comprobaciones de los casos
comprobar_caso_1 = False
comprobar_caso_2 = False
comprobar_caso_3 = False
while turnos <= 9 and comprobar_caso_1 == False and comprobar_caso_2 == False and comprobar_caso_3 == False:

    #posiciones
    posicion_x = 0
    posicion_y = 0

    #comprobacion de posiciones
    comprobar_posiciones = False

    #condicional para turnar entre jugadores
    if turnos % 2 != 0:
        print(f"Turno {turnos} - jugador 1")
        
        print("indique fila-columna: ")
        #posiciones
        posicion_x = int(input("filas: "))
        posicion_y = int(input("columnas: "))
        
        while comprobar_posiciones == False:
            #bucle para que no salga de los limites
            while (posicion_x < 0 or posicion_x > 2) or (posicion_y < 0 or posicion_y > 2):
                print("fuera de indice o posicion ocupada, pruebe con otro valor en filas-columnas")
                posicion_x = int(input("filas: "))
                posicion_y = int(input("columnas: "))

            #comprobamos que no este ocupado por x ó o
            if tablero[posicion_x][posicion_y] == "x" or tablero[posicion_x][posicion_y] == "o":
                print("posicion ocupada, pruebe con otras filas-columnas")
                posicion_x = int(input("filas: "))
                posicion_y = int(input("columnas: "))
                comprobar_posiciones = False
            else:
                tablero[posicion_x][posicion_y] = jugador1
                comprobar_posiciones = True
        
    else:
        print(f"Turno {turnos} - jugador 2")

        print("indique fila-columna: ")
        
        #posiciones
        posicion_x = int(input("filas: "))
        posicion_y = int(input("columnas: "))
        
        #condicional para turnar entre jugadores

        while comprobar_posiciones == False:
            
            #bucle para que no salga de los limites
            while (posicion_x < 0 or posicion_x > 2) or (posicion_y < 0 or posicion_y > 2):
                print("fuera de indice o posicion ocupada, pruebe con otro valor en filas-columnas")
                posicion_x = int(input("filas: "))
                posicion_y = int(input("columnas: "))

            #comprobamos que no este ocupado por x ó o
            if tablero[posicion_x][posicion_y] == "x" or tablero[posicion_x][posicion_x] == "o":
                print("posicion ocupada, pruebe con otras filas-columnas")
                posicion_x = int(input("filas: "))
                posicion_y = int(input("columnas: "))
                comprobar_posiciones = False
            else:
                tablero[posicion_x][posicion_y] = jugador2
                comprobar_posiciones = True
    
    #caso 1: verificar que no esten iguales en filas

    if tablero[0][0] == tablero[0][1] and tablero[0][1] == tablero[0][2] and tablero[0][0] == tablero[posicion_x][posicion_y]:
        print("1 fila")
        comprobar_caso_1 = True
    elif tablero[1][0] == tablero[1][1] and tablero[1][1] == tablero[1][2] and tablero[1][0] == tablero[posicion_x][posicion_y]:
        print("2 fila")
        comprobar_caso_1 = True
    elif tablero[2][0] == tablero[2][1] and tablero[2][1] == tablero[2][2] and tablero[2][0] == tablero[posicion_x][posicion_y]:
        print("3 fila")
        comprobar_caso_1 = True
    
    #caso 2: verificar que no esten iguales en columnas

    if tablero[0][0] == tablero[1][0] and tablero[1][0] == tablero[2][0] and tablero[0][0] == tablero[posicion_x][posicion_y]:
        #primer columna
        comprobar_caso_2 = True
    elif tablero[0][1] == tablero[1][1] and tablero[1][1] == tablero[2][1] and tablero[0][1] == tablero[posicion_x][posicion_y]:
        #segunda columna
        comprobar_caso_2 = True
    elif tablero[0][2] == tablero[1][2] and tablero[1][2] == tablero[2][2] and tablero[0][2] == tablero[posicion_x][posicion_y]:
        #tercer columna
        comprobar_caso_2 = True
    
    #caso 3: verificar que no esten iguales en filas

    if tablero[0][0] == tablero[1][1] and tablero[1][1] == tablero[2][2] and tablero[0][0] == tablero[posicion_x][posicion_y]:
        #diagonal principal
        comprobar_caso_3 = True
    elif tablero[2][0] == tablero[1][1] and tablero[1][1] == tablero[0][2] and tablero[2][0] == tablero[posicion_x][posicion_y]:
        #diagonal secundaria
        comprobar_caso_3 = True
    
    #imprimimos el tablero
    print("     0    1    2")
    print(f"0  {tablero[0]}")
    print(f"1  {tablero[1]}")
    print(f"2  {tablero[2]}")

    #incrementamos los turnos
    turnos+=1
    print("--------------------")


if comprobar_caso_1:
    #Caso 1 - Fila
    if tablero[posicion_x][posicion_y] == jugador1:
        print("Jugador 1 ganador!")
    elif tablero[posicion_x][posicion_y] == jugador2:
        print("Jugador 2 ganador!")
elif comprobar_caso_2:
    #Caso 2 - Columna
    if tablero[posicion_x][posicion_y] == jugador1:
        print("Jugador 1 ganador!")
    elif tablero[posicion_x][posicion_y] == jugador2:
        print("Jugador 2 ganador!")
elif comprobar_caso_3:
    #Caso 3 - Diagonal
    if tablero[posicion_x][posicion_y] == jugador1:
        print("Jugador 1 ganador!")
    elif tablero[posicion_x][posicion_y] == jugador2:
        print("Jugador 2 ganador!")
else:
    print("empate")