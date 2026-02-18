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
        self.cargar_desde_archivo() #se carga automaticamebte al iniciar

    def cargar_desde_archivo(self):
        """
        se cargan los productos desde el archivo inventario.txt
        si este archivo no existe, lo crea automaticamente

        """
        try:
            with open("inventario.txt","r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(",")
                    #validamos que la linea tenga los 4 datos necesarios
                    if len (datos) == 4:
                        id_producto = datos[0]
                        nombre = datos[1]
                        precio = float(datos[2])
                        cantidad = float(datos[3])

                        #creamos el objeto producto
                        producto = Producto(id_producto, nombre, precio, cantidad)
                        self.productos.append(producto)
            print("inventario cargado correctamente desde el archivo")
        except FileNotFoundError:
            #si el archivo no existe, lo crea automaticamente
            open("inventario.txt","w").close()
            print("archivo inventario.txt creado porque no existia")
        except PermissionError:
            print("error: no tienes permisos para leer este archivo")
        except Exception as e:
            print(f"error inesperado al cargar el archivo: {e}")

    def guardar_en_archivo(self):
        """
        se guardan todos los productos actuales en el archivo inventario.txt
        sobrescribe el contenido cada vez que se llama

        """
        try:
            with open("inventario.txt","w") as archivo:
                for p in self.productos:
                    linea =f"{p.get_id()},{p.get_nombre()},{p.get_precio()},{p.get_cantidad()} \n"
                    archivo.write(linea)
            print("cambios guardados correctamente en el archivo")
        except PermissionError:
            print("error: no tienes permisos para escribir este archivo")
        except Exception as e:
            print(f"error inesperado al guardar el archivo: {e}")

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
        self.guardar_en_archivo()
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