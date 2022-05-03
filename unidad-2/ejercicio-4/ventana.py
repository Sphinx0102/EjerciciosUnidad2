class Ventana():
    __titulo = None
    __value_coor_sup_iz_x = None
    __value_coor_sup_iz_y = None
    __value_coor_inf_der_x = None
    __value_coor_inf_der_y = None

    #Contructor
    def __init__(self,tit='', vcsix=0, vcsiy=0, vcidx=0, vcidy=0):
        self.__titulo = tit
        self.__value_coor_sup_iz_x = vcsix
        self.__value_coor_sup_iz_y = vcsiy
        self.__value_coor_inf_der_x = vcidx
        self.__value_coor_inf_der_y = vcidy
    
    #metodo1
    def mostrar(self):
        print('Titulo: {}, Vertise superior izquierdo: ({},{}), Vertice inferior derecho: ({},{})'.format(self.__titulo, self.__value_coor_inf_der_x,self.__value_coor_inf_der_y,self.__value_coor_sup_iz_x,self.__value_coor_sup_iz_y))
    
    #metodo2
    def getTitulo(self):
        return(self.__titulo)
    
    #metodo3
    def alto(self):
        if(self.__value_coor_inf_der_y > self.__value_coor_sup_iz_y):
            return (self.__value_coor_inf_der_y - self.__value_coor_sup_iz_y)


    #metodo4
    def ancho(self):
        if(self.__value_coor_sup_iz_x > self.__value_coor_inf_der_x):
            return (self.__value_coor_inf_der_x - self.__value_coor_sup_iz_x)
    
    #metodo5
    def moverDerecha(self, movimiento = 1):
        if(self.__value_coor_inf_der_x > self.__value_coor_sup_iz_x):
            self.__value_coor_inf_der_x += movimiento
            self.__value_coor_sup_iz_x += movimiento

    #metodo6    
    def moverIzquierda(self, movimiento = 1):
        if(self.__value_coor_inf_der_x > self.__value_coor_sup_iz_x):
            self.__value_coor_inf_der_x -= movimiento
            self.__value_coor_sup_iz_x -= movimiento

    #metodo7
    def subir(self, movimiento = 1):
        if(self.__value_coor_inf_der_y > self.__value_coor_sup_iz_y):
            self.__value_coor_inf_der_y += movimiento
            self.__value_coor_sup_iz_y += movimiento

    #metodo8
    def bajar(self, movimiento = 1):
        if(self.__value_coor_inf_der_y > self.__value_coor_sup_iz_y):
            self.__value_coor_inf_der_y -= movimiento
            self.__value_coor_sup_iz_y -= movimiento
        