from personal import Personal
import numpy as np
import csv

class Personal_handler:
    __lista = []

    def __repr__(self):
       return str(self.__lista)

    def carga_personal(self):
        file = open('personal.csv')
        csvreader = csv.reader(file, delimiter = ';')
        bandera = True
        for row in csvreader:
            if(bandera):
                bandera = not bandera
            else:
                legajo = row[0]
                dni = row[1]
                apellido = row[2]
                nombre = row[3]
                sueldo_basico = row[4]
                new_personal = Personal(legajo, dni, apellido, nombre, sueldo_basico)
                self.__lista.append(new_personal)
        file.close()
        return self.__lista

    def get_array(self):
        array = np.array(self.__lista)
        return array

    def saldo_liquidar(self, lista):
        i = 0 
        while i < len(self.__lista):
            j = 0
            while j < len(lista):
                if(self.__lista[i].get_legajo() == lista[j].get_legajo()):
                    if(lista[j].get_codigo() == 'A'):
                        numero = (lista[j].get_importe())
                        self.__lista[i].calculo_adicion(numero)
                    if(lista[j].get_codigo() == 'D'):
                        numero = (lista[j].get_importe())
                        self.__lista[i].calculo_descuento(numero)
                j += 1
            self.__lista[i].get_sueldo()
            i += 1
        
        

    def consulta_sueldo(self):
        legajo = input("ingrese el numero de legajo a consultar: \n")
        i = 0
        while i < len(self.__lista):
            if(self.__lista[i].get_legajo() == legajo):
                print("El sueldo a liquidar es de: {}".format(self.__lista[i].get_sueldo_liquidar()))
            i += 1


    def __sort_list(self):
        longitud = len(self.__lista)
        for i in range(longitud -1):
            for j in range(i+1, longitud):
                if(self.__lista[j] < self.__lista[i]):
                    self.__lista[j], self.__lista[i] = self.__lista[i], self.__lista[j]
        return self.__lista


    def sueldo_mas_bajo(self):
        lista_sorted = self.__sort_list()
        print("el sueldo a liquidar mas bajo es de: {}".format(lista_sorted[0].get_sueldo_liquidar()))
    