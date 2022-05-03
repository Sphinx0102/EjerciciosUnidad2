class Registro():
    __temperatura  = None
    __humedad = None
    __presion_atmosferica = None
    
    #Constructor
    def __init__(self, temperatura= '', humedad= '', presion = ''):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presion_atmosferica = presion

    def registro (self, dia):
        self.___dia = dia[0]
        self.__hora = dia[1]
        self.__temperatura = dia[2]
        self.__humedad = dia[3]
        self.__presion_atmosferica = dia[4]