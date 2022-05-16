from proyectoHandler import ProyectoList
from integranteProyectoHandler import IntegranteLista


def main():
   listaProyecto = ProyectoList()
   Arreglo = IntegranteLista()
   listaProyecto.carga_proyecto()
   array = Arreglo.carga_integrantes()
   listaProyecto.calculoPuntos(array)
   listaProyecto.mostrarData(array)



if __name__ == "__main__":
    main()