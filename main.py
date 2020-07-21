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
    print('1  - Consulta 1 (se esfecifica) ')
    print('2 - Consulta dos ')
    print('3 - Consulta tres ')
    print('4 - Consulta cuatro ')
    print('5 - Consulta cinco ')


print('----------------------------------------------------------------------')
print('             Trabajo Final: Gestion de Bases de Datos                  ')
print('                 Base de Datos: DynamoDB AMAZON                        ')
print('----Integrantes: ')
print('-------> Anto lo mas')
print('-------> Anto lo mas')
print('-------> Anto lo mas')
print('-------> Anto lo mas')
print('-------> Anto lo mas')

x = input()


salir = False
while salir == False:
    screen_clear()
    menuOpciones()
    x = input('Elija una opcion de consulta\n')
    if x == '1':
        print('---Consulta uno----')
        x = input()
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
    
