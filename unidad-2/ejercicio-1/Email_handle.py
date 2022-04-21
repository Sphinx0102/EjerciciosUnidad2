import re
from Email import Email


class Email_handle():
    __email_list = None

    #Constructor
    def __init__(self, emails=[]):
        self.__email_list = emails

    def agregar_email(self, email_label):
        email = Email()
        email.crear_cuenta(email_label)
        self.__email_list.append(email)

    def validar_id_cuenta(self, id_cuenta):
        index = 0

        while index < len(self.__email_list) and not re.search(id_cuenta, self.__email_list[index].retorna_email().split('@')[0]):
            index += 1

        if index < len(self.__email_list):
            print('El identificador esta repetido')
        else:
            print('El identificador no se ha encontrado')
