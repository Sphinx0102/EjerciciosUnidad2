from novedades import Novedad
import numpy as np
import csv


class Novedades_handler:
    __lista = []

    def __repr__(self):
        return str(self.__lista)

    def carga_novedades(self):
        file = open('novedades.csv')
        csvreader = csv.reader(file, delimiter = ';')
        bandera = True
        for row in csvreader:
            if(bandera):
                bandera = not bandera
            else:
                legajo = row[0]
                importe = row[1]
                concepto = row[2]
                codigo = row[3]
                new_novedad = Novedad(legajo, importe, concepto, codigo)
                self.__lista.append(new_novedad)
        file.close()
        return self.__lista

    def get_lista(self):
        return self.__lista
    
    def __sort_array(self, array):
        #array_sorted = np.sort([i.get_nombre() for i in array])
        #print(array_sorted)            
        longitud = len(array)
        for i in range(longitud -1):
            for j in range(i+1, longitud):
                if (array[i] > array[j]):
                    #fuuuuuusion aah
                    array[i], array[j] = array[j], array[i]
        return array

    def listar_data(self, array):
        array_sorted = self.__sort_array(array)
        # [print("""apellido: {}       nombre: {}\ndni: {}\nsueldo basico: ${}"""
        # .format(i.get_apellido(), i.get_nombre(), i.get_dni(), i.get_sueldo_basico())) for i in array_sorted]
        i = 0
        while i < len(array_sorted):
            j = 0
            print("""apellido: {}       nombre: {}\ndni: {}\nsueldo basico: ${}"""
            .format(array_sorted[i].get_apellido(), array_sorted[i].get_nombre(), array_sorted[i].get_dni(), array_sorted[i].get_sueldo_basico()))
            print("""Codigo:      Concepto:                importe:\n""")
            while j < len(self.__lista):
                if(self.__lista[j].get_legajo() == array_sorted[i].get_legajo()):
                    print("  {}            {}                 {} \n"
                    .format(self.__lista[j].get_codigo(),self.__lista[j].get_concepto() , self.__lista[j].get_importe() ))
                j += 1
            print("Total a cobrar: ${} \n".format(array_sorted[i].get_sueldo_liquidar()))
            i += 1
        
            

                


    