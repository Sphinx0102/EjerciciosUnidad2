from Cama import Cama
from datetime import datetime
import csv

class camaHandler():

    def __init__(self):
        self.__lista_cama = []


    def busqueda_nombre(self, key):
        for i in range(len(self.__lista_cama)):
            if(key == self.__lista_cama[i].getName()):
                value = datetime.now()
                self.__lista_cama[i].mostrarData(value)
                return self.__lista_cama[i].getIdCama()

    def busqueda_diagnostico(self, key):
        for i in range(len(self.__lista_cama)):
            if(self.__lista_cama[i].getDiagnostico(key)):
                if(self.__lista_cama[i].getEstado()):
                   print(self.__lista_cama[i].mostrarData())

    def carga_cama(self):
        file = open('camas.csv')
        csvreader = csv.reader(file, delimiter = ';')
        for row in csvreader:
            id_cama = row[0]
            habitacion = row[1]
            estado = row[2]
            nombre = row[3]
            diagnostico = row[4]
            fecha_internacion = row[5]
            fecha_alta = row[6]
            newcama = Cama(id_cama, habitacion, estado, nombre, diagnostico, fecha_internacion, fecha_alta)
            self.__lista_cama.append(newcama)
        file.close()
        return self.__lista_cama