from PlanAhorro import PlanAhorro


class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.opcion4,
                            '5':self.salir
                          }
    def opcion(self,op, list):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op=='2' or op=='3' or op=='4':
            func(list)
        else:
            func()
    def salir(self):
        print('Usted salio del programa')
    def opcion1(self,list):
        for index in range(len(list)):
            list[index].getdata()
            nuevo_valor = input("ingrese el valor actual del vehiculo: ")
            print("Valor actual del vehiculo: {}" .format(list[index].modificar_valor(nuevo_valor)))
        
    def opcion2(self,list):
        valor = int (input("Ingrese el valor de la cuota a comparar: "))
        for index in range(len(list)): 
            if(list[index].cuota() < valor):
                list[index].getdata()
            else:
                print("ningun plan tiene un valor de cuota menor al proporcionado")
                break

    def opcion3(self, list):
        index = input("Ingrese el numero del plan a consultar: ")
        monto = list[index].licitacion() * list[index].cuota
        print("El monto a pagar para licitar es: {}" .format(monto))
    
    def opcion4(self, list):
        index = input("Ingrese el numero del plan a consultar: ")
        valor= input("Ingrese las cantidad de cuotas que desea modificar: ")
        print("la cantidad de cuotas ahora es: {}" .format(list[index].licitacion(valor)))

