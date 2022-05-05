from Registro import Registro


class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.salir
                          }
    def opcion(self,op, lista):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op=='2' or op=='3':
            func(lista)
        else:
            func()
    def salir(self):
        print('Usted salio del programa')
    def opcion1(self,lista):
        max_value = 0
        min_value = 9999
        auxindex_i= 0
        auxindex_j = 0
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                
                    
                
        
    def opcion2(self,list):
       

    def opcion3(self, list):
       
