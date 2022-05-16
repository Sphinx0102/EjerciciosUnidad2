from clase import Clase
import csv

def carga_archivo(nameFile):
    lista = []
    file = open(nameFile)
    csvreader = csv.reader(file)
    for row in csvreader:
        id = row[0]
        name = row[1]
        born = row[2]
        newclase = Clase(id, name, born)
        lista.append(newclase)
    return(lista)

def fun_reverse(lista):
    lista.reverse()
    print(lista)


def main():
    lista = carga_archivo('dataset.csv')
    fun_reverse(lista)


if __name__ == '__main__':
    main()