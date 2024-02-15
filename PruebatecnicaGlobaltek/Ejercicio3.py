# creamos una funcion 
def agrupar_elementos_similares():
    # crearemos una lista vacia para que el usuario indique los numeros que desee
    lista = []
    #inicie un bucle sin fin, hasta que el usuario ingrese la palabra "fin" valga la redundancia
    while True:
        # le solicito al usuario que ingrese el numero que desee y "fin" para terminar
        num = input("Ingrese un número (o 'fin' para terminar): ")
        if num.lower() == 'fin':
            break
        # esta parte solo la hice para que el codigo rectifique si en verdad es un numero y no una letra
        try:
            lista.append(int(num)) # se agrega a la lista si el numero es valido
        except ValueError:
            print("Por favor, ingrese un número válido.") # se imprime un mensaje para que el usuario rectifique un numero

# creo una clase llamado matriz, para guardar la entrada de datos que ingrese el uusuario 
    matriz = {}
    for elemento in lista:
        if elemento in matriz:
            matriz[elemento] += 1 # lo agrega si el numero ya esta, ejemplo {2, 2}
        else:
            matriz[elemento] = 1 # si el elemento no esta en la matriz, se agrega con el conteo desde 1 

# creo la salida en este caso de la matriz para almacenar los elementos agrupados
    salida = []
    # iteramos cada elemento y cantidad en la matriz
    for elemento, cantidad in matriz.items():
        # se crea un grupo de la matriz que contendra el elemento repetido 
        grupo = [elemento] * cantidad
        # se agrega esta lista a la salida
        salida.append(grupo)

    return salida

# resultados 
resultado = agrupar_elementos_similares()
print("Matriz de elementos agrupados:", resultado)
