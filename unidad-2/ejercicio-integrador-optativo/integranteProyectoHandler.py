from integranteProyecto import IntegranteProyecto
import csv
import numpy as np

class IntegranteLista:
    __lista = []

    def carga_integrantes(self):
        file = open('integrantesProyecto.csv')
        csvreader = csv.reader(file, delimiter = ';')
        bandera = True
        for row in csvreader:
            if bandera:
                bandera = not bandera
            else:
                idProyecto = row[0]
                apellidoNombre = row[1]
                dni = row[2]
                categoriaInvestigacion = row[3]
                rol = row[4]
                newintegrante = IntegranteProyecto(idProyecto, apellidoNombre, dni, categoriaInvestigacion, rol)
                self.__lista.append(newintegrante)
        array = np.array(self.__lista)
        file.close()
        return (array)

    