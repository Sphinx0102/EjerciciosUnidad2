class email():
    #Constructor
    def __init__(self, idCuenta, dominio, tipoDomino, contraseña):
        self.__idCuenta = idCuenta;
        self.__dominio = dominio;
        self.__tipoDomino = tipoDomino;
        self.__contraseña = contraseña;
    #Metodo 1
    def retornaEmail(self):
        return(self.__idCuenta + '@' + self.__dominio + '.' + self.__tipoDomino);
    #Metodo 2
    def getDominio(self):
        return('@'+ self.__dominio);
    #Metodo 3
    def crearCuenta(self, name):
        return('Estimado ' 
            + name 
            + ' te enviaremos tus mensajes a la direccion:' 
            + self.__idCuenta 
            + '@' 
            + self.__dominio 
            + '.' 
            + self.__tipoDomino);

if __name__ == '__main__':
    unEmail = email('leo','gmail', 'com', '123abc');
    print(unEmail.crearCuenta('leo'));
    