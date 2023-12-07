from repartidor import Repartidor
import csv

class RepartidorHandler():
    __lista = []

    def cargar_repartidor(self):
        file = open('repartidores.csv')
        csvreader = csv.reader(file, delimiter = ';')
        bandera = True
        for row in csvreader:
            if bandera:
                bandera = not bandera
            else:
                id = row[0]
                apellido = row[1]
                nombre = row[2]
                telefono = row[3]
                movilidad = row[4]
                comision = row[5]
                new_repartidor = Repartidor(id, apellido, nombre, telefono, movilidad, comision)
                self.__lista.append(new_repartidor)
        file.close()

    def get_lista(self):
        return self.__lista