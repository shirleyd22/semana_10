#la clase Productos representa cada postre o producto que se vende en la pasteleria

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        """
        constructor de la clase Producto
        este se ejecuta automaticamente cuando se crea
        un nuevo objeto

        :para id: identificador unico del producto
        :para nombre: nombre del producto
        :para cantidad: cantidad disponible en el inventario
        :para precio: precio unitario del producto
        """
        #atributos privados ( encapsulacion)
        # se usan __ para asi evitar que estos se modifiquen directamente
        self.__id = id
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    #metodos getters: permiten obtener el valor de los atributos
    def get_id(self):
        return self.__id
    def get_nombre(self):
        return self.__nombre
    def get_cantidad(self):
        return self.__cantidad
    def get_precio(self):
        return self.__precio

    #metodos setters: estos permiten modificar los atributos privados

    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_cantidad(self, cantidad):
        self.__precio = cantidad
    def set_precio(self, precio):
        self.__precio = precio

    #metodo especial para mostrar el objeto de forma legible cuando se imprime en pantalla

    def __str__(self):
        return f"ID: {self.__id} | {self.__nombre} | Cantidad {self.__cantidad} | Precio: ${self.__precio: .2f}"
