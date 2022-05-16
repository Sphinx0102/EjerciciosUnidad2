class Proyecto:
    __idProyecto = None
    __titulo = None
    __palabrasClave = None
    __puntos = int

    def __init__(self, idProyecto = '', titulo = '', palabrasClave = ''):
        self.__idProyecto = idProyecto
        self.__titulo  = titulo
        self.__palabrasClave = palabrasClave
        self.__puntos = int(0)

    def getId(self):
        return self.__idProyecto
    
    def agregarPuntos(self, punto):
        puntos = int(punto)
        self.__puntos = self.__puntos + puntos
        print("se sumaron {}".format(puntos))
        return (self.__puntos)
    
    def restarPuntos(self, punto):
        puntos = int(punto)
        self.__puntos = self.__puntos - puntos
        print("se restaron {}".format(puntos))
        return(self.__puntos)


    def getPuntos(self):
        return self.__puntos

    def __gt__(self, valor):
        return self.__puntos > valor

