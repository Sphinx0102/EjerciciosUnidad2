from pedidosHandler import PedidosHandler
from repartidoresHandler import RepartidorHandler

def main():
    lista_repartidores = RepartidorHandler()
    lista_repartidores.cargar_repartidor()
    arreglo_pedidos = PedidosHandler()
    arreglo_pedidos.cargar_pedido()

    bandera = True  
    while bandera:
        print("""--------------------------------------- \n
        Menu
                1: Sueldo a liquidar por legajo
                2: Listar alfabeticamente
                3: Sueldo mas bajo a liquidar
                4: salir \n
---------------------------------------""")
        opcion = input("Ingrese la opcion deseada: \n")
        if(opcion == '1'):
            i= 0
            
        # elif(opcion == '2'):
           
        # elif(opcion == '3'):
            
        elif(opcion == '4'):
            print("Usted a salido del programa")
            bandera = not bandera


if __name__ == '__main__':
    main()