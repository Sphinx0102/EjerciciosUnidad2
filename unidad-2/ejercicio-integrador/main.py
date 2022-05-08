from numpy import diag
from mediHandler import mediHandler
from camaHandler import camaHandler




def main():
    lista_cama = camaHandler()
    lista_medicamento = mediHandler()
    lista_cama.carga_cama()
    lista_medicamento.carga_medicamento()
    nombre = input("Ingrese el nombre del paciente al que se le da el alta: ")
    index = lista_cama.busqueda_nombre(nombre)
    lista_medicamento.busqueda_idCama(index)
    diagnostico = input("Ingrese el diagnostico del paciente: ")
    lista_cama.busqueda_diagnostico(diagnostico)




if __name__ == '__main__':
    main()






