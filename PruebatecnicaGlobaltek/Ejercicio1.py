# creamos una funcion en este caso llamada suma_Serie, la cual dentro de esta clase creamos dos entradas.
# numero y la otra es terminos, todo esto en numeros enteros con la ayuda de la funcion "int" , esto con que el usuario ingrese los numeros que desee.
def suma_serie():
    numero = int(input("Ingrese un número para la serie: "))
    terminos = int(input("Ingrese el número de términos de la serie: "))
    
    
    suma = 0
    multiplicador = 1

# en esta parte del codigo crearemos el bucle de la ecuacion, sabemos que la suma va desde 0 y multiplicador desde 1.
# esto con la funcion de que el bucle se ejecute cada vez por cada termino que indiquemos
    for i in range(terminos):
        #creamos la ecuaacion que tomara el numero y luego lo multiplicara por el numero de terminos
        terminos = int(str(numero) * multiplicador)
        # en el caso de la suma se agrega el termino dado por el usuario a la suma total
        suma += terminos
        # en el caso del multiplicador, lo incrementamos uno mas para la suma total
        multiplicador += 1

        #retornamos a la suma de todos los terminos de la serie que indiquemos
    return suma

# llamamos la funcion, para que calcule y luego la imprimimos en la pantalla de la terminal
resultado = suma_serie()
print("La suma de la serie es:", resultado)
