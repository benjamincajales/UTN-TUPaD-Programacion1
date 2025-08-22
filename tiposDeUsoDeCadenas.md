Uso de cadenas de caracteres
ingresando el texto
x = "a las palabras se las lleva el viento"
Los caracteres de las cadenas se numeran desde 0 en adelante
1-Obtenga en pantalla utilizando print:
    a. El caracter ubicado en la primera posicion, acompañado de la tercera
        print(x[0],x[2])
        # salida: al
    b. Todos los caracteres contenidos en la variable x, desde el primero y
    tomando de 3 en 3, hasta el decimo
        print(x:10:3)
        #salida:aapa
    c. La longitud total de la cadena de x.
        print(len(x))
        #salida: 37
    d. Muestra toda la cadena con la primera letra en mayuscula
        print(x.capitalize())
        #salida: A las palabras se las lleva el viento
    e. Muestra toda la cadena en mayusculas
        print(x.upper())
        #salida: A LAS PALABRAS SE LAS LLEVA EL VIENTO
    f. Muestre toda la cadena en minuscula
        y = "Las Luces de la calle tienen HOY UN Brillo ESPECIAL"
        print(y.lower())
        #salida: 
    g. Muestra la cadena inviertiendo mayusculas y minusculas
        y = "Las Luces de la calle tienen HOY UN Brillo ESPECIAL"
        print(y.swapcase())
        #salida: lAS LUCES DE LA CALLE TIENEN hoy un bRILLO ESPECIAL
