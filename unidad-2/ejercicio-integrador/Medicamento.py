class Medicamento():
    __id_cama = None
    __id_medicamento = None
    __nombre_com = None
    __monodroga = None
    __presentacion = None
    __cantidad_apl = None
    __precio = None

    def __repr__(self):
        return str(self.__dict__)
        
    def getIdCama(self):
        return self.__id_cama
    
    def mostrarData(self):
        print("      {}/{}             {}        {}           {}".format(self.__nombre_com, self.__monodroga
        , self.__presentacion, self.__cantidad_apl, self.__precio))
    
    def getPrecio(self):
        return self.__precio

    def __init__(self, id_cama = '', id_medicamento = '',nombre_com = '', monodroga = '', presentacion = '', cantidad = '', precio = ''):
        self.__id_cama = int(id_cama)
        self.__id_medicamento = int(id_medicamento)
        self.__nombre_com = nombre_com
        self.__monodroga = monodroga
        self.__presentacion = presentacion
        self.__cantidad_apl = int(cantidad)
        self.__precio = float(precio)