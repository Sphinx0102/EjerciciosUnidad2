from pedido import Pedido
import numpy as np
import csv


class PedidosHandler():
    __lista = []

    
    def cargar_pedido(self):
        file = open('pedidos.csv')
        csvreader = csv.reader(file, delimiter = ";")
        bandera = True
        for row in csvreader:
            if bandera:
                bandera = not bandera

            else:
                id = row[0]
                numero_pedido = row[1]
                descripcion = row[2]
                cantidad = row[3]
                precio_unitario = row[4]
                estado = row[5]
                new_pedido = Pedido(id, numero_pedido, descripcion, cantidad, precio_unitario, estado)
                self.__lista.append(new_pedido)
        file.close()

    def get_array(self):
        array = np.array(self.__lista)
        return array
            