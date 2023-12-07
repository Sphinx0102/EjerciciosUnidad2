class Pedido():
    __id = None
    __numero_pedido = None
    __descripcion = None
    __cantidad = None
    __precio_unitario = None
    __estado = None


    def __init__(self, id = '', numero_pedido = '', descripcion = '', cantidad = '', precio_unitario = '', estado = ''):
        self.__id = id
        self.__numero_pedido = numero_pedido
        self.__descripcion = descripcion
        self.__cantidad = cantidad
        self.__precio_unitario = int(precio_unitario)
        self.__estado = estado

