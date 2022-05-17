class Personal:
    __legajo = None
    __dni = None
    __apellido = None
    __nombre = None
    __sueldo_basico = None
    __sueldo_liquidar = None

    def __repr__(self):
        return str(self.__dict__)

    def __init__(self, legajo = '', dni = '', apellido = '', nombre = '', sueldo_basico = ''):
        self.__legajo = legajo
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldo_Basico = int(sueldo_basico)
        self.__sueldo_liquidar = int(0)

    def get_legajo(self):
        return self.__legajo

    def calculo_adicion(self, numero):
        adicion = int(numero)
        self.__sueldo_liquidar += adicion
        print("Se le sumo {}".format(adicion))
    
    def calculo_descuento(self, numero):
        descuento = int(numero)
        self.__sueldo_liquidar -= descuento
        print("se le resto {}".format(descuento))

    def get_sueldo(self):
        self.__sueldo_liquidar += self.__sueldo_Basico
        return self.__sueldo_liquidar

    def __gt__(self, value):
        self.__nombre > value
