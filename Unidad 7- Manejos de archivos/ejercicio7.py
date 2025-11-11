import os
NOMBRE_ARCHIVO = 'productos.txt'

#1. crear archivo inicial de nombre productos.txt
def crear_archivo():
    productos_iniciales = '''Lapicera,120.5,30
Cuaderno,350.75,15
Regla,50.0,50'''
    ""
    with open(NOMBRE_ARCHIVO,'w',newline="",encoding='utf-8') as f:
        f.write(productos_iniciales)

#2. Leer y mostrar archivo
def mostrar_archivo():
    with open(NOMBRE_ARCHIVO,'r') as archivo:
        print("-- Productos --")
        for linea in archivo:
            linea_limpia = linea.strip()
            #separamos los parametros
            nombre, precio, cantidad = linea_limpia.split(",")

            print(f"Productos: {nombre} | Precio: $ {float(precio)} | Cantidad: {int(cantidad)}")

#3. Agregar productos desde teclado
def agregar_productos():
    print("-- agregar un nuevo producto --")
    opc = input("quiere agregar un producto (s/n): ")
    match opc:
        case 's':
            with open(NOMBRE_ARCHIVO,'a',encoding='utf-8') as archivo:
                #ingresamos nombre
                nombre_ingresado = input("ingrese un nombre: ")
                #ingresamos precio
                precio = input("ingrese un precio: ")
                #ingresamos cantidad
                cantidad = input("ingrese una cantidad: ")
                #agregamos los nuevos productos
                nueva_linea = (f"\n{nombre_ingresado.capitalize()},{precio},{cantidad}")
                archivo.write(nueva_linea)
                #imprimimos por pantalla la nueva linea
                print("se agrego correctamente el nuevo producto")
            #mostramos el archivo cambiado
            mostrar_archivo()
        case 'n':
            pass
        case _:
            print("opcion incorrecta")


#mostrar lista cargada
def mostrar_lista(lst):
    for linea in lst:
        print(f"Producto: {linea['nombre']} | Precio: {linea['precio']} | Cantidad: {linea['cantidad']}")

#4. cargar productos en una lista de diccionarios
def cargar_txt():
    print("-- cargar productos a una lista --")
    lista_diccionario = []
    with open(NOMBRE_ARCHIVO,'r') as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            #salta las lineas vacias
            if not linea_limpia:
                continue
            #separamos los parametros
            nombre, precio, cantidad = linea_limpia.split(",")
            productos_dict = {
                "nombre": nombre,
                "precio": precio,
                "cantidad":cantidad
            }
            lista_diccionario.append(productos_dict)
    return lista_diccionario

#5. buscar producto por nombre
def buscar_producto(lst):
    print("-- buscar producto --")
    producto_buscado = input("ingrese el producto a buscar: ")
    for i in lst:
        #si lo encuentra muestra mensaje y retorna
        if i['nombre'] == producto_buscado.capitalize():
            print("El producto es: ")
            print(i)
            return
    #si no lo encuentra retorna y muestra mensaje
    print("No se encuentra el producto")
    return 

if not os.path.exists(NOMBRE_ARCHIVO):
    crear_archivo()
print(" ")
mostrar_archivo()
print(" ")
agregar_productos()
print(" ")
lista = cargar_txt()
mostrar_lista(lista)
print(" ")
buscar_producto(lista)