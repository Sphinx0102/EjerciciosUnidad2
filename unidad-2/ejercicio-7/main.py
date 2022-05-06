from Viajero_frecuente import Viajero_frecuente
import csv
import sys

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



def mayormillas(list):
    auxindex = 0
    max = 0
    for i in range(len(list)):
        if(list[i] > list[(i+1) != range(len(list)+1)]):
            max = list[i].cantidadTotalMillas()
            auxindex = i
        else:
            max = list[i+1].cantidadTotalMillas()
            auxindex = i+1
    print("el viajero: {} con mas millas tienen: {}".format(list[auxindex].getnro(), max))


def acumularmillas(list):
    nro = input("Ingrese el numero de viajero: ")
    for i in range(len(list)):
        if(list[i].getnro() == nro):
            print("el viajero: {} retorna ahora una instancia de tipo: {} ".format(nro, list[i] + 100))
            break


def canjearmilla(list):
    nro = input("Ingrese el numero de viajero: ")
    for i in range(len(list)):
        if(list[i].getnro() == nro):
            print("el viajero: {} retorna ahora una instancia de tipo: {} ".format(nro, list[i] - 100))
            break      
 

def comparamillas(list):
    nro = input("Ingrese el numero de viajero: ")
    for i in range(len(list)):
        if(list[i].getnro() == nro):
            if(list[i] == 100):
                print("Las millas son las mismas")
            if(100 == list[i]):
                print("Las millas son las mismas")
            break
        
def newacumularmillas(list):
    nro = input("Ingrese el numero de viajero: ")
    for i in range(len(list)):
        if(list[i].getnro() == nro):
            list[i] = 100 + list[i]
            print("el viajero: {} retorna ahora una instancia de tipo: {} ".format(nro, list[i]))            
            break


def newcanjearmilla(list):
    nro = input("Ingrese el numero de viajero: ")
    for i in range(len(list)):
        if(list[i].getnro() == nro):
            list[i] = 100 - list[i]
            print("el viajero: {} retorna ahora una instancia de tipo: {} ".format(nro, list[i]))             
            break



def main():
    list = carga_archivo()
    #nro = input("Ingrese el numero de viajero ")
    #busqueda(nro,list)

    #mayormillas(list)
    #acumularmillas(list)
    #canjearmilla(list)
    comparamillas(list) #Numero de viajero 70 tiene cargadas 100 millas
    newacumularmillas(list)
    newcanjearmilla(list)

if __name__ == '__main__':
    main()
