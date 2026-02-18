#importamos las clases necesarias

from servicios.inventario import Inventario
from modelos.producto import Producto

#esta funcion muestra el menu en la consola
def mostrar_menu():
    print("\n === Sistema de Inventario - Pasteleria dulce sabor ===")
    print("1. añador producto")
    print("2. eliminar producto")
    print("3. actualizar producto")
    print("4. buscar producto")
    print("5. mostrar inventario")
    print("6. salir")

#funcion principal del programa
def main():
    #se crea una isntancia de inventario
    inventario = Inventario()
    #bucle infinito para que el menu pueda repetirse
    while True:
        mostrar_menu()
        opcion= input("por favor seleccione una opcion: ")
        #anadir producto
        if opcion == "1":
            try:
                id=int(input("Ingrese el ID del producto: "))
                nombre=input("Ingrese el nombre del producto: ")
                cantidad=int(input("Ingrese el cantidad de producto: "))
                precio=float(input("Ingrese el precio del producto: "))
                #se crea el objeto producto
                producto = Producto(id,nombre,precio, cantidad)
                #se lo añade al inventario
                inventario.add_producto(producto)
            except ValueError:
                print("Error: debe ingresar valores numericos validos ")
        #eliminar productos
        elif opcion == "2":
            try:
                id=int(input("Ingrese el ID del producto que se va a eliminar: "))
                inventario.eliminar_producto(id)
            except ValueError:
                print("el ID no es valido")
        #actualizar producto
        elif opcion == "3":
            try:
                id=int(input("Ingrese el ID del producto a actualizar: "))
                cantidad = input("nueva cantidad ( presione enter para omitir)")
                precio = input("nuevo precio ( presione enter para omitir")

                #convertimos solo si el usuario ingresa los datos
                nueva_cantidad = int(cantidad) if cantidad else None
                nuevo_precio = float(precio) if precio else None

                inventario.actualizar_producto(id, nueva_cantidad, nuevo_precio)
            except ValueError:
                print("Error: estos datos no son validos ")
        #buscar productos

        elif opcion == "4":
            nombre = input("por favor ingrese el nombre que desea buscar: ")
            inventario.buscar_producto(nombre)
        #mostrar el inventario
        elif opcion == "5":
            inventario.mostrar_inventario()
        #salir
        elif opcion == "6":
            print("grcias por usar nuestro sistema")
            break
        else:
            print("opcion no valida")
if __name__ == "__main__":
    main()