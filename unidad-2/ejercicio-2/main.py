from Viajero_frecuente import Viajero_frecuente
import csv

def carga_archivo():
    list = []
    file = open('dataset.csv')
    csvreader= csv.reader(file)
    for row in csvreader:
        viajero = Viajero_frecuente()
        viajero.registrar_viajero(row)
        list.append(viajero)
    return(list)
    

def busqueda(nro, list):
    print("prueba")
    for i in range(len(list)):
        print("prueba")
        print(list[i].getnro())
        if (list[i].getnro() == nro):
            print("""Menu: 
            Opcion 1: Consultar cantidad de Millas
            Opcion 2: Acumular Millas
            Opcion 3: Canjear Millas""")
            opcion = input("ingrese el numero de la opcion deseada:")
            menu(opcion, list, i)



def menu (opcion, list, i):
    if(opcion == "1"):
        print("Las millas acumuladas son {}" .format(list[i].cantidadTotalMillas()))
    elif(opcion == "2"):
        millas = input("Ingrese las millas a acumular ")
        print("Millas acumuladas {}" .format(list[i].acumularMillas(millas)))
    elif(opcion == "3"):
        millas = input("ingrese las millas a canjear ")
        print("Millas actuales {}" .format(list[i].canjearMillas(millas)))
    else:
        print("La opcion ingresada no es correcta")


def main():
    list = carga_archivo()
    nro = input("Ingrese el numero de viajero ")
    busqueda(nro,list)


if __name__ == '__main__':
    main()
