class Email():
    __id_cuenta = None
    __dominio = None
    __tipo_dominio = None
    __contrasenia = None

    #Constructor
    def __init__(self, id_cuenta='', dominio='', tipo_dominio='', contrasenia=''):
        self.__id_cuenta = id_cuenta
        self.__dominio = dominio
        self.__tipo_dominio = tipo_dominio
        self.__contrasenia = contrasenia

    #Metodo 1
    def retorna_email(self):
        return(self.__id_cuenta + '@' + self.__dominio + '.' + self.__tipo_dominio);

    #Metodo 2
    def get_dominio(self):
        return('@'+ self.__dominio);

    def set_contrasenia(self, contrasenia):
        self.__contrasenia = contrasenia

    def get_contrasenia(self):
        return self.__contrasenia

    #Metodo 3
    def crear_cuenta(self, email):
        first_email_array = email.split('@')
        self.__id_cuenta = first_email_array[0]
        second_email_array = first_email_array[1].split('.')
        self.__dominio = second_email_array[0]
        self.__tipo_dominio = second_email_array[1]
