class Viajero_frecuente():
    __num_viajero = None
    __dni = None
    __nombre = None
    __apellido = None
    __millas_acum = None

    #Constructor
    def __init__(self,num_viajero='',dni='',nombre='',apellido='',millas_acum=''):
        self.__num_viajero=num_viajero
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millas_acum=millas_acum

    #metodo0
    def getnro(self):
        return self.__num_viajero

    #metodo1
    def cantidadTotalMillas(self):
        return self.__millas_acum
    
    #metodo2
    def acumularMillas(self, milla):
        millas = int(milla)
        self.__millas_acum+=millas
        return self.__millas_acum
    
    #metodo3
    def canjearMillas(self, milla_canje):
        millas_canje = int(milla_canje)
        if(millas_canje <= self.__millas_acum):
            self.__millas_acum-=millas_canje
        else:
            print("Error en la operacion")
        return self.__millas_acum 

    #metodo4
    def registrar_viajero(self, viajero):
        self.__num_viajero = viajero[0]
        self.__dni = viajero[1]
        self.__nombre = viajero [2]
        self.__apellido = viajero [3]
        self.__millas_acum = int(viajero[4])


        

    
