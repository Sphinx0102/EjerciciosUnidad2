import numpy as np
from Registro import Registro
import csv


def carga_archivo():
    list_hora = []
    list_dia = []
    file = open('dataset.csv')
    cvsreader = csv.reader(file)
    for dia in cvsreader:
        registro = Registro()
        registro




def main():
    registro = Registro()
    carga_archivo()


if __name__=='__main__':
    main()