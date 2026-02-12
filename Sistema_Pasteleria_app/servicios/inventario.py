#importamos la clase Producto desde la carpeta modelos

from modelos.producto import Producto
#la case inventario se encarga de gestionar todos los productos que se encuentran en la pasteleria

class Inventario:
    def __init__(self):
        """
        constructor de la clase Inventario
        se crea una lista vacia donde se almacenaran los productos
        """
        self.productos = []
    #metodo para añadir producto
    def add_producto(self, producto):
        """
        añade un nuevo producto al inventario
        antes de agegarlo, se valida que el id no este repetido
        """
        for p in self.productos:
            if p.get_id ()== producto. get_id():
                print("Error: ya existe un producto con este ID ")
                return
                #se sale del metodo si el ID esta repetido
        #si el ID no esta repetido se lo agrega
        self.productos.append(producto)
        print("producto agregado correctamente")
    #metodo para buscar productos
    def buscar_producto(self, nombre):
        """
        busca productos por coincidencia parcial en el nombre
        No importa si el usuario escribe en mayusculas o minisculas
        """
        encontrados = []
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                encontrados.append (p)
        if encontrados:
            print("productos encontrados: ")
            for p in encontrados:
                print(p)
        else:
            print("no se encontraron productos con ese nombre")
    #metodo para mostrar el inventario
    def mostrar_inventario(self):
        """
        muestra todos los productos que se encuetran almacenados
        """
        if not self.productos:
            print("el inventario se encuentra vacio")
        else:
            print("inventario actual: ")
            for p in self.productos:
                print(p)