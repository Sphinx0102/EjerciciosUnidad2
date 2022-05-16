from proyecto import Proyecto
import csv

class ProyectoList:
    __lista = []

    def carga_proyecto (self):
        file = open('proyectos.csv')
        csvreader = csv.reader(file, delimiter = ';')
        bandera = True
        for row in csvreader:
            if bandera:
                bandera = not bandera
            else:
                idProyecto = row[0]
                titulo = row[1]
                palabrasClave = row[2]
                newproyecto = Proyecto(idProyecto, titulo, palabrasClave)
                self.__lista.append(newproyecto)
        file.close()
        return self.__lista

    
    def calculoPuntos(self, array):
        i = 0
        while(i < len(self.__lista)):
            j=0
            aux1 = 0
            aux2 = 0
            cont = 0
            while(j < len(array)):
                if(self.__lista[i].getId() == array[j].getId()):
                    cont +=1
                    if(array[j].getRol() == 'director'):
                        aux1 += 1
                        if((array[j].getCategoria() == 'I') or (array[j].getCategoria() == 'II')):
                            self.__lista[i].agregarPuntos(10)
                        else:
                            self.__lista[i].restarPuntos(5)
                            print('El director debe tener como minimo categoria I o II')

                    elif(((array[j].getRol() == 'codirector') or (array[j].getRol() != 'integrante')) and 
                    ((array[j].getCategoria() == 'I') or (array[j].getCategoria() == 'II') or (array[j].getCategoria() == 'III'))):
                        aux2 +=1
                        self.__lista[i].agregarPuntos(10)
                    elif((array[j].getRol() != 'codirector') and (array[j].getRol() != 'integrante')):
                            self.__lista[i].restarPuntos(5)
                            print('El codirector debe tener como minimo categoria III')
                    elif(((array[j].getRol() == 'codirector') and (array[j].getRol() != 'integrante')) and 
                    ((array[j].getCategoria() == 'IV') or (array[j].getCategoria() == 'V'))):
                            self.__lista[i].restarPuntos(5)
                            print('El codirector debe tener como minimo categoria III')
                j+=1
            
            if(aux1 > 1 and aux1 != 0): print("El Proytecto debe tener un director")
            elif(aux2 > 1 and aux2 != 0): print("El Proyecto debe tener un codirector")
            if(aux1 == 0 and aux2 == 0): self.__lista[i].restarPuntos(10)
            if(cont >= 3):
                self.__lista[i].agregarPuntos(10)
            else: 
                print("El proyecto debe de tener como minimo 3 integrantes")
                self.__lista[i].restarPuntos(20)
            print("Puntaje del proyecto{} es de : {}".format(self.__lista[i].getId(), self.__lista[i].getPuntos()))
            i+=1
 

    def mostrarData(self, array):
        i = 0
        while i+1 < (len(self.__lista)):
            if(self.__lista[i].getPuntos() > self.__lista[i+1].getPuntos()):
                print("prueba")
            else:
                print("noPrueba")
            i+=1