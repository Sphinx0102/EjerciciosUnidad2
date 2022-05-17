from novedades import Novedad
from personal import Personal
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
    
    def listar_data(self, array):
        array.sort()
        print(array)
            

                


    