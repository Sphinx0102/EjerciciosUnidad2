from Conjunto import Conjunto
from claseMenu import Menu

    


def main():
    
    A= Conjunto([1,2,3,4])
    B = Conjunto([4,6,9])



    bandera = False
    while not bandera:
        print("""Menu: 
            Opcion 1: La unión de dos conjuntos
            Opcion 2: La diferencia de dos conjuntos
            Opcion 3: Verificar si dos conjuntos son iguales
            Opcion 4: Salir""")
        opcion = input("ingrese el numero de la opcion deseada: ")
        menu = Menu()
        menu.opcion(opcion, A, B)
        bandera = int(opcion) == 4


if __name__=='__main__':
    main()