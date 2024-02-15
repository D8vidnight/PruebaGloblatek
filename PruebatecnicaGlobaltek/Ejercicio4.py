# Creamos una clase llamada inventario ya que todo se guardara en esta parte del codigo, se inicia con las 3 categorias
class Inventario:
    def __init__(self):
        self.inventario = {'dairy': {}, 'cleaning': {}, 'grain': {}} # cada categoria estara asociada a los productos y sus existencias en el espacio "{}" 

    # metodo para agregar productos al inventario, dando el dato del producto, la cantidad y el grupo que pertenece 
    def registrar_producto(self, nombre, cantidad, grupo):
        if grupo in self.inventario: # si el producto ya existe en el grupo, actualizara el usuario las cantidades de este
            if nombre in self.inventario[grupo]:
                self.inventario[grupo][nombre] += cantidad
            else:
                self.inventario[grupo][nombre] = cantidad 
        else: # si el grupo no existe en el inverntario, mandara error 
            print("El grupo especificado no existe en el inventario.")

    # metodo para mostrar el inventario 
    def mostrar_inventario(self):
        print("Inventario:")
        for grupo, productos in self.inventario.items(): # se llama todas las categorias guardadas en la variable "self.inventario" para imprimirlos en la consola
            print(f"Grupo: {grupo.capitalize()}")
            for producto, cantidad in productos.items():
                print(f"  Producto: {producto}, Existencias: {cantidad}")
        print("---------------------------------")

# metodo de interaccion del usuario 
def interactuar_usuario():
    inventario = Inventario() # creamos una clase llamada inventario
    while True: # Mostraremos el menu princiálmente para la interaccion del usuario 
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        # opciones para el menu
        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            grupo = input("Ingrese el grupo del producto (dairy/cleaning/grain): ")
            inventario.registrar_producto(nombre, cantidad, grupo)
        elif opcion == "2":
            inventario.mostrar_inventario()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else: # si no es una opcion valida como 1,2,3. mandaremos un mensaje de error 
            print("Opción no válida. Por favor, seleccione una opción válida.")
        print("----------------------------------")


if __name__ == "__main__":
    interactuar_usuario()

