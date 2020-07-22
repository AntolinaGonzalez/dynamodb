from Funciones_Querys import *
from os import system, name
from time import sleep


def screen_clear():
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear')

def menuOpciones():
    print('---------------Menu-----------------')
    print('1  - Dado un anio se devuelve el ganador y sus respectivos jugadores ')
    print('2 - Consulta dos ')
    print('3 - Consulta tres ')
    print('4 - Consulta cuatro ')
    print('5 - Consulta cinco ')


print('----------------------------------------------------------------------')
print('             Trabajo Final: Gestion de Bases de Datos                  ')
print('                 Base de Datos: DynamoDB AMAZON                        ')
print('----Integrantes: ')
print('-------> Badaro Maximiliano')
print('-------> Cao Luis Gonzalo')
print('-------> Gonzalez Antolina')
print('-------> Mambrin Ventre Jonathan')
print('-------> Rolon Tomas')

x = input()


salir = False
while salir == False:
    screen_clear()
    menuOpciones()
    x = input('Elija una opcion de consulta\n')
    if x == '1':
        print('---Consulta uno----')
        x = int(input('Ingrese un anio \n'))
        mostrarPantalla(jugadores_equipo_campeon(x))
        x=input()
    elif x == '2':
        print('---Consulta dos----')
        x = input()
    elif x == '3':
        print('---Consulta tres----')
        x = input()
    elif x == '4':
        print('---Consulta cuatro----')
        x = input()
    elif x == '5':
        print('---Consulta cinco----')
        x = input()
    else:
        salir = True
    
