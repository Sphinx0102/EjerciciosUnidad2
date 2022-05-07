from Registro import Registro
from claseMenu import Menu
import csv

def carga_archivo():
    lista_dia = [[0] * 24 for i in range(30)]
    file = open('dataset.csv')
    csvreader = csv.reader(file, delimiter = ',')
    for row in csvreader:
        index_i = int(row[0])
        index_j = int(row[1])
        temp = row[2]
        hum = row[3]
        pre = row[4]
        newregistro = Registro(temp, hum, pre)
        lista_dia[index_i-1][index_j]=newregistro
    file.close()
    return(lista_dia)



def main():
    lista = carga_archivo()

    bandera = False
    while not bandera:
        print("""Menu: 
            Opcion 1: Mostrar dia y hora de el menor y mayor valor de las variables
            Opcion 2: Indicar la temperatura promedio mensual por cada hora
            Opcion 3: Listar los valores de las tres variables para cada hora del día dado
            Opcion 4: Salir""")
        opcion = input("ingrese el numero de la opcion deseada: ")
        menu = Menu()
        menu.opcion(opcion, lista)
        bandera = int(opcion) == 4



if __name__=='__main__':
    main()