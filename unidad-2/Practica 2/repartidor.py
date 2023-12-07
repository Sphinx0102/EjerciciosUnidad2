class Repartidor():
    __id = None
    __apellido = None
    __nombre = None
    __telefono = None
    __movilidad = None
    __comision = None

    def __init__(self, id = '', apellido = '', nombre = '', telefono = '', movilidad = '', comision = ''):
        self.__id = id
        self.__apellido  = apellido
        self.__nombre = nombre
        self.__telefono = telefono
        self.__movilidad = movilidad
        self.__comision = int(comision)