from Funciones_Querys import *
from os import system, name
from time import sleep


def screen_clear():
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear')

def menuOpciones():

    print('---------------------------Menu---------------------------\n')
    print('\t1 - Paises participantes de la Copa Mundial \n\t    a partir de un año ingresado  \n')
    print('\t2 - Cantidad de goles en una Copa Mundial  \n\t    a partir de un año y pais ingresado  \n')
    print('\t3 - Consulta tres ')
    print('\t4 - Consulta cuatro ')
    print('\t5 - Consulta cinco ')
    print('\t0 - Salir')



print('-----------------------------------------------------------------------')
print('             Trabajo Final: Gestion de Datos                           ')
print('                  Gestor: DynamoDB AMAZON                              ')
print('-----------------------------------------------------------------------')
print('----Integrantes: ')
print('-------> Badaro Maximiliano')
print('-------> Cao Luis Gonzalo')
print('-------> Gonzalez Antolina')
print('-------> Mambrin Ventre Jonathan')
print('-------> Rolon Tomas')

input()




while True:
    
    screen_clear()
    
    menuOpciones()
    
    op = ('0', '1', '2', '3', '4', '5')

    x = input('Elija una opcion de consulta\n')
    
    screen_clear()
    
    while x not in op:
        
        menuOpciones()
        x = input('Elija una opcion de consulta\n')
        screen_clear()

    if x == '1':
        
        y =input('\tIngrese un año para consultar:\t')
        screen_clear()

        print('\n\n\tPaises participantes del año: '+ y + "\n")
        
        for pais in paises_participantes_edicion_particular(y):

            print("\t\t",pais)

        
        input("\nPresione cualquier tecla para volver al menu")



    elif x == '2':

        print("\tEdiciones: ", ediciones)
        z = input('\n\tIngrese un año:\t')
        screen_clear()
        print(f"\tPaises participantes para el año: {z}\n")

        paises = paises_participantes_edicion_particular(z)

        cont = 0

        for i in range(len(paises) // 5): 
            print()
            for j in range(5): 

                if cont == len(paises):
                    break
                else: 
                    print("|  "+ paises[cont], end=' |')
                    cont += 1    

        
        y = input('\n\n\tIngrese un pais para consultar:\t')
        
        screen_clear()
        
        while es_pais_edicion_particular(y, z) == False:

            print("\tEdiciones: ", ediciones)
            z = input('\n\tIngrese un año:\t')
            screen_clear()
            print(f"\tPaises participantes para el año: {z}\n")

            paises = paises_participantes_edicion_particular(z)

            cont = 0

            for i in range(len(paises) // 5): 
                print()
                for j in range(5): 

                    if cont == len(paises):
                        break
                    else: 
                        print("|  "+ paises[cont], end=' |')
                        cont += 1    
        
        screen_clear()
            


        print(f"\n\n\tCantidad de goles del equipo {y} en el año {z} : {cantidad_goles_edicion_particular(y, z)}")

        input("\nPresione cualquier tecla para volver al menu")
       

        
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
        break