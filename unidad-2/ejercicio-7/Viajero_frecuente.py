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

    def __repr__(self):
        return str(self.__dict__)

    #metodo0
    def getnro(self):
        return self.__num_viajero

    #metodo1
    def cantidadTotalMillas(self):
        return self.__millas_acum

    def __gt__(self, objet):
        return self.__millas_acum > objet.cantidadTotalMillas()
    
    def __eq__(self, milla):
        if((self.__millas_acum == milla) 
            or (milla == self.__millas_acum)):
            return True
        return False

    
    #metodo2
    def acumularMillas(self, milla):
        millas = int(milla)
        self.__millas_acum+=millas
        return self.__millas_acum

    def __add__(self, milla):
        millas = int(milla)
        self.__millas_acum += millas
        return Viajero_frecuente(0,0,0,0,self.__millas_acum)
    
    def __radd__(self, milla):
        millas = int(milla) 
        self.__millas_acum += millas
        return Viajero_frecuente(0,0,0,0,self.__millas_acum)
            

    #metodo3
    def canjearMillas(self, milla_canje):
        millas_canje = int(milla_canje)
        if(millas_canje <= self.__millas_acum):
            self.__millas_acum-=millas_canje
        else:
            print("Error en la operacion")
        return self.__millas_acum 

    def __sub__(self, milla):
        millas = int(milla)
        if(millas <= self.__millas_acum):
            self.__millas_acum-=millas
        else:
            print("Error en la operacion")
        return Viajero_frecuente(0,0,0,0,self.__millas_acum)


    def __rsub__(self, milla):
        millas = int(milla)
        if(millas <= self.__millas_acum):
            self.__millas_acum-=millas
        else:
            print("Error en la operacion")
        return Viajero_frecuente(0,0,0,0,self.__millas_acum)

    #metodo4
    def registrar_viajero(self, viajero):
        self.__num_viajero = viajero[0]
        self.__dni = viajero[1]
        self.__nombre = viajero [2]
        self.__apellido = viajero [3]
        self.__millas_acum = int(viajero[4])


        

    
