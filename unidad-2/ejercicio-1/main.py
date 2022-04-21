from Email import Email
from Email_handle import Email_handle
import csv


def registrar_user():
    nombre = input('Ingrese nombre: ')
    id_cuenta = input('Ingresar identificador de cuenta: ')
    dominio = input('Ingresar dominio: ')
    tipo_dominio = input('Ingresar tipo de dominio: ')
    contrasenia = input('Ingresar contraseña: ')
    email = Email(id_cuenta, dominio, tipo_dominio, contrasenia)
    print('Estimado {0} te enviaremos tus mensajes a la direccion {1}'.format(nombre, email.retorna_email()))
    return email

def cambiar_contrasenia(email):
    contrasenia = input('Ingrese su contraseña: ')

    if contrasenia == email.get_contrasenia:
        nueva_contrasenia = input('Ingrese nueva contraseña: ')
        email.set_contrasenia(nueva_contrasenia)
    else:
        print('Contraseña incorrecta')

def registrar_email():
    email_label = input('Ingrese una cuenta de correo: ')
    email = Email()
    email.crear_cuenta(email_label)
    print('Email creado: {0}'.format(email.retorna_email()))

def cargar_archivo():
    email_handle = Email_handle()
    file = open('dataset.csv')
    csvreader = csv.reader(file)
    rows = []

    for row in csvreader:
        email_handle.agregar_email(row[0])

    email_handle.validar_id_cuenta(input('Ingresar identificador de una cuenta: '))

def main():
    email = registrar_user()
    cambiar_contrasenia(email)
    registrar_email()
    cargar_archivo()

if __name__ == '__main__':
    main()
