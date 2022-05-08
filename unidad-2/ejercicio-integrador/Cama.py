class Cama():
    __id_cama = None
    __habitacion = None
    __estado = None
    __nombre = None
    __diagnostico = None
    __fecha_internacion = None
    __fecha_alta = None

    def __repr__(self):
        return str(self.__dict__)
        
    def getName(self):
        return self.__nombre
    
    def getIdCama(self):
        return self.__id_cama
    
    def mostrarData(self, value = ''):
        self.__fecha_alta = value
        print("""\nPaciente: {}  Cama: {}   Habitacion: {}
Diagnostico : {}  Fecha de internacion: {}
Fecha de alta: {}\n""".format(self.__nombre, self.__id_cama, self.__habitacion
        , self.__diagnostico, self.__fecha_internacion, self.__fecha_alta))


    def getDiagnostico(self, value):
        if(value == self.__diagnostico):
            return True
        else:
            return False

    def getEstado(self):
        return self.__estado


    def __init__(self, id_cama = '',habitacion = '', estado = '', nombre = '' , diagnostico = '', fecha_internacion = '', fecha_alta = ''):
        self.__id_cama = int(id_cama)
        self.__habitacion = habitacion
        self.__estado = bool(estado)
        self.__nombre = nombre
        self.__diagnostico = diagnostico
        self.__fecha_internacion = fecha_internacion
        self.__fecha_alta = fecha_alta
