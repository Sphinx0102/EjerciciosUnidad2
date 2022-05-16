class Clase():
    __id = None
    __nombre = None
    __nacimiento = None


    def __init__(self, id = '', nombre = '', nacimiento = ''):
        self.__id = id
        self.__nombre = nombre
        self.__nacimiento = nacimiento

    def __repr__(self):
        return str(self.__dict__)
    