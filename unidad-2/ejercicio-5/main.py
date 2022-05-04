from PlanAhorro import PlanAhorro
from claseMenu import Menu
import csv


def carga_archivo ():
    list = []
    file = open('dataset.csv')
    csvreader = csv.reader(file)
    for row in csvreader:
        plan = PlanAhorro()
        plan.registrar_plan(row)
        list.append(plan)
    return list





def main():
    list = carga_archivo()
    list[1].cuota()


    bandera = False
    while not bandera:
        print("""Menu: 
            Opcion 1: Actualizar Valor Vehicular de cada Plan
            Opcion 2: Mostrar datos
            Opcion 3: Monto para licitar
            Opcion 4: Modificar cantidad de cuotas para licitar
            Opcion 5: Salir""")
        opcion = input("ingrese el numero de la opcion deseada: ")
        menu = Menu()
        menu.opcion(opcion, list)
        bandera = int(opcion) == 5


if __name__ == '__main__':
    main()