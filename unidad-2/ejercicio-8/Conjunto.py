import collections


class Conjunto():
    __arreglo = []


    def __init__(self, array = []):
        self.__arreglo = array

    def __repr__(self):
        return str(self.__dict__)

    def get(self):
        return self.__arreglo

    def __add__(self, array2):
        array1=self.__arreglo
        array1.extend(array2.get())
        return list(set(array1))

    
    def __sub__(self, array2):
        array1=self.__arreglo
        diferencia1 = (set(array1).difference(array2.get()))
        diferencia2 = (set(array2.get()).difference(array1))
        list_differencia = list(diferencia1.union(diferencia2))
        return list_differencia

    def __eq__(self, array2):
        array1=self.__arreglo
        if(collections.Counter(array1) == collections.Counter(array2.get())):
            return True
        else:
            return False