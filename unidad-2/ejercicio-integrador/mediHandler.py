from Medicamento import Medicamento
import csv

class mediHandler():


    def __init__(self):
        self.__lista_medicamento = []

    def busqueda_idCama(self, key):
        acum = 0
        print("""Medicamento/Monodroga                   Presentacion     Cantidad      Precio \n""")
        for i in range(len(self.__lista_medicamento)):
            if(key == self.__lista_medicamento[i].getIdCama()):
                self.__lista_medicamento[i].mostrarData()
                acum +=self.__lista_medicamento[i].getPrecio()
        print("\nTotal adeudado:                                                      {}".format(acum))

    def carga_medicamento(self):
        file = open('medicamentos.csv')
        csvreader = csv.reader(file)
        for row in csvreader:
            id_clase = int(row[0])
            id_medicamento = int(row[1])
            nombre_com = row[2]
            monodroga = row[3]
            presentacion = row[4]
            cantidad = row[5]
            precio = row[6]
            newmedicamento = Medicamento(id_clase, id_medicamento, nombre_com, monodroga, presentacion, cantidad, precio )
            self.__lista_medicamento.append(newmedicamento)
        file.close()
        return self.__lista_medicamento