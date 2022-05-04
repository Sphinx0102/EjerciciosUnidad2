
class PlanAhorro():
    __codigo_plan = None
    __modelo = None
    __version_vehiculo = None
    __valor_vehiculo = None
    __cuotas_total = None
    __cuotas_licitar = None

    def __init__(self, codigo = '', modelo = '', version = '', valor = '', cuotas_total = '', cuotas_licitar = ''):
        self.__codigo_plan = codigo
        self.__modelo = modelo
        self.__version_vehiculo = version
        self.__valor_vehiculo = valor
        self.__cuotas_total = cuotas_total
        self.__cuotas_licitar = cuotas_licitar
    

    def cuota (self):
        valor_cuota= (self.__valor_vehiculo / self.__cuotas_total) + self.__valor_vehiculo * 0.10
        return valor_cuota


    def registrar_plan(self, plan):
        self.__codigo_plan = plan[0]
        self.__modelo = plan[1]
        self.__version_vehiculo = plan[2]
        self.__valor_vehiculo = float (plan[3])
        self.__cuotas_total = int (plan[4])
        self.__cuotas_licitar = int (plan[5])

    def getdata(self):
        print("Codigo de plan: {} , Modelo: {} , Version: {}" .format(self.__codigo_plan, self.__modelo, self.__version_vehiculo))


    def modificar_valor(self, valor):
        val = int(valor)
        self.__valor_vehiculo = val
        return self.__valor_vehiculo

    def licitacion(self, valor = 0):
        val = int(valor)
        if(valor == 0):
            cuotas_restantes = self.__cuotas_licitar
        else:
            cuotas_restantes = val
        return cuotas_restantes
    
    
