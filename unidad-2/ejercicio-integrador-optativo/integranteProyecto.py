class IntegranteProyecto:
    __idProyecto = None
    __apellidoNombre = None
    __dni = None
    __categoriaInvestigacion = None
    __rol = None

    def __init__(self, idProyecto = '', apellidoNombre = '', dni = 0, categoriaInvestigacion = '', rol = ''):
        self.__idProyecto = idProyecto
        self.__apellidoNombre = apellidoNombre
        self.__dni = int(dni)
        self.__categoriaInvestigacion = categoriaInvestigacion
        self.__rol = rol

    def getId(self):
        return self.__idProyecto

    def getRol(self):
        return self.__rol
    
    def getCategoria(self):
        return self.__categoriaInvestigacion