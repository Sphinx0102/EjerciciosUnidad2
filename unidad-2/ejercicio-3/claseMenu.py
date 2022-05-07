from unittest import result
from Registro import Registro
import numpy as np




def comparation_fun(lista, key, type = 'min'):
    max = 0
    min = 9999
    auxindex_i = 0
    auxindex_j = 0
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if(isinstance(lista[i][j], Registro)):  
                result = getattr(lista[i][j], key)()
                if(type == 'max'):
                    if(result > max):
                        max = result
                        auxindex_i = i
                        auxindex_j = j
                else:
                    if(result < min):
                        min = result
                        auxindex_i = i
                        auxindex_j = j
    
    print("para la variable el {} fue el dia: {} a la hora: {}".format(type, auxindex_i, auxindex_j))
    

def promedio_temp(lista, j):
    acum = 0
    cont = 0
    for i in range(len(lista)):
        if(isinstance(lista[i][j], Registro)):
            acum += lista[i][j].getvalue_temp()
            cont +=1

    return acum/cont


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
        print("Temperatura:")
        comparation_fun(lista, 'getvalue_temp', 'max')
        comparation_fun(lista, 'getvalue_temp')
        print("Humedad:")
        comparation_fun(lista, 'getvalue_humedad', 'max')
        comparation_fun(lista, 'getvalue_humedad')  
        print("Presion:")
        comparation_fun(lista, 'getvalue_presion', 'max')
        comparation_fun(lista, 'getvalue_presion')  

    def opcion2(self,lista):
        j = int(input("ingrese la hora a consultar: "))
        promedio = promedio_temp(lista, j)         
        print("la temperatura promedio mensual para la hora: {} es de: {}°C".format(j, promedio))

    def opcion3(self, lista):
        i = int(input("Ingrese el dia a consultar: "))
        for j in range(len(lista[i])):
            if(isinstance(lista[i][j], Registro)):
                print("""Hora:   Temperatura:   Humedad:   Presion:""")
                print("   {}          {}           {}         {}".format(j, lista[i][j].getvalue_temp(), lista[i][j].getvalue_humedad(), lista[i][j].getvalue_presion()))
        
