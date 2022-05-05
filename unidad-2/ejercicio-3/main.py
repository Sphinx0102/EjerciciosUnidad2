import numpy as np
from Registro import Registro
from claseMenu import Menu
import csv

def define_list():
    file = open('dataset.csv')
    csvreader = csv.reader(file)
    max_dia = 0
    max_hora = 0
    for row in csvreader:
        if(int(row[0]) > max_dia):
            max_dia = int(row[0])
        if(int(row[1]) > max_hora):
            max_hora = int(row[1])
    return [['no data'] * (max_hora+1) for i in range(max_dia)]

def carga_archivo():
    lista = define_list()
    file = open('dataset.csv')
    cvsreader = csv.reader(file)
    for row in cvsreader:
        registro = Registro()
        registro.registro(row)
        lista[int(row[0])-1][int(row[1])] = registro



def main():
    carga_archivo()

    bandera = False
    while not bandera:
        print("""Menu: 
            Opcion 1: Mostrar dia y hora de el menor y mayor valor de las variables
            Opcion 2: Mostrar datos
            Opcion 3: Monto para licitar
            Opcion 4: Modificar cantidad de cuotas para licitar
            Opcion 5: Salir""")
        opcion = input("ingrese el numero de la opcion deseada: ")
        menu = Menu()
        menu.opcion(opcion, list)
        bandera = int(opcion) == 4



if __name__=='__main__':
    main()