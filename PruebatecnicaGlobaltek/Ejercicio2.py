# se crea la funcion llamada retorno
def retorno():
    # se inicia una lista para que guarde los datos ingresados por el usuario 
    lista = []
    # se inicia el bucle while, hasta que el usuario decida terminar con "fin"
    while True:
        num = input("Ingrese un número (o 'fin' para terminar): ")
        if num.lower() == 'fin': 
            break
        try:
            lista.append(int(num)) # la entrada se convertira en numero entero, si el usuario escribe otra cosa que no sea entero, mandara un error
        except ValueError:
            print("Por favor, ingrese un número válido.")

    # se inicia otra lista para que almacene los numeros de acuerdo a las condiciones dadas
    salida = []
    for num in lista:
        if num % 5 == 0: # condicion 1, el numero que sea divisible por cinco
            if num > 600: # condicion 2, si el numero es mayor a 600, no se incluye en la salida
                continue
            elif num > 1000: # condicion 3, si el numero es mayor a 1000, detenga el procedimiento y retorne el resultado
                return salida
            else:
                salida.append(num) # si el numero cumple con alguna de las condiciones se guardara en la lista
    return salida

# resultado
resultado = retorno()
print("Números especiales encontrados:", resultado)
