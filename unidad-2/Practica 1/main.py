from novedadesHandler import Novedades_handler
from personalHandler import Personal_handler

def main():
    lista_novedades = Novedades_handler()
    lista_novedades.carga_novedades()
    arreglo_personal = Personal_handler()
    arreglo_personal.carga_personal()
    

    #cargar saldo a liquidar
    arreglo_personal.saldo_liquidar(lista_novedades.get_lista())
    
    bandera = True  
    while bandera:
        print("""---------------------------------------
Menu
        1: Sueldo a liquidar por legajo
        2: Listar alfabeticamente
        3: Sueldo mas bajo a liquidar
        4: salir
---------------------------------------""")
        opcion = input("Ingrese la opcion deseada: \n")
        if(opcion == '1'):
            arreglo_personal.consulta_sueldo()
        elif(opcion == '2'):
            lista_novedades.listar_data(arreglo_personal.get_array())
        elif(opcion == '3'):
            arreglo_personal.sueldo_mas_bajo()
        elif(opcion == '4'):
            print("Usted a salido del programa")
            bandera = not bandera



if __name__=='__main__':
    main()