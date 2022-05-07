class Registro():
    __temperatura  = None
    __humedad = None
    __presion_atmosferica = None
    
    #Constructor
    def __init__(self, temperatura= '', humedad= '', presion = ''):
        self.__temperatura = int(temperatura)
        self.__humedad = int(humedad)
        self.__presion_atmosferica = int(presion)


    def getvalue_temp(self):
        return self.__temperatura
    
    def getvalue_humedad(self):
        return self.__humedad

    def getvalue_presion(self):
        return self.__presion_atmosferica