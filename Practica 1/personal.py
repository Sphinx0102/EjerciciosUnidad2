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
        self.__sueldo_basico = int(sueldo_basico)
        self.__sueldo_liquidar = int(0)

    def get_legajo(self):
        return self.__legajo

    def calculo_adicion(self, numero):
        adicion = int(numero)
        self.__sueldo_liquidar += adicion
    
    def calculo_descuento(self, numero):
        descuento = int(numero)
        self.__sueldo_liquidar -= descuento

    def get_sueldo(self):
        self.__sueldo_liquidar += self.__sueldo_basico
        return self.__sueldo_liquidar

    def get_sueldo_liquidar(self):
        return self.__sueldo_liquidar

    def __gt__(self, value):
        return self.__nombre > value.get_nombre()

    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido

    def get_sueldo_basico(self):
        return self.__sueldo_basico
    
    def get_apellido(self):
        return self.__apellido
    
    def get_dni(self):
        return self.__dni
    
    def __lt__(self, value):
        return self.__sueldo_liquidar < value.get_sueldo_liquidar()
