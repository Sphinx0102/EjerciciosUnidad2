class Registro():
    __temperatura  = None
    __humedad = None
    __presion_atmosferica = None
    
    #Constructor
    def __init__(self, temperatura= '', humedad= '', presion = ''):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presion_atmosferica = presion

    def getvalue_temp(self):
        return self.__temperatura
    
    def getvalue_humedad(self):
        return self.__humedad

    def getvalue_presion(self):
        return self.__presion_atmosferica

    def registro (self, dia):
        self.___dia = dia[0]
        self.__hora = dia[1]
        self.__temperatura = int(dia[2])
        self.__humedad = int(dia[3])
        self.__presion_atmosferica = int(dia[4])