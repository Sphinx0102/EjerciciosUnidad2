class Novedad:
    __legajo = None
    __importe = None
    __concepto = None
    __codigo = None

    def __repr__(self):
        return str(self.__dict__)

    def __init__(self, legajo = '', importe = '', concepto = '', codigo = ''):
        self.__legajo = legajo
        self.__importe = float(importe)
        self.__concepto = concepto
        self.__codigo = codigo
    
    def get_legajo(self):
        return self.__legajo

    def get_importe(self):
        return self.__importe
    
    def get_codigo(self):
        return self.__codigo
    
    def get_concepto(self):
        return self.__concepto