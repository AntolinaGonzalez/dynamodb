from Funciones_Querys import *



portada()



while True:
    
    x = '6'

    op = ('0', '1', '2', '3', '4', '5')
    
    while x not in op:

        screen_clear()
        
        menuOpciones()

        x = input('\n\n\tElija una opcion de consulta:\t')
        
    screen_clear()   


#----------------------------------------------------------------
    if x == '1':

        print('\n\t1 - Paises participantes de la Copa Mundial a partir de un año ingresado  \n\n')

        y = 0

        while int(y) not in ediciones: 

            imprimir_Lista_n_columnas(ediciones, 10 )

            y =input('\n\n\tIngrese un año para consultar:\t')

            screen_clear()

        print('\n\n\tPaises participantes del año: '+ y + "\n")
        
        for pais in paises_participantes_edicion_particular(y):

            print("\t\t",pais)

        
        input("\nPresione cualquier tecla para volver al menu")


    #----------------------------------------------------------------------------------------------------
    elif x == '2':

        z = 0

        y = ' '
          
        while int(z) not in ediciones: 

            print('\n\t2 - Cantidad de goles en una Copa Mundial a partir de un año y pais ingresado  \n\n')

            imprimir_Lista_n_columnas(ediciones, 10 )

            z =input('\n\n\tIngrese un año para consultar:\t')

            screen_clear()

        
        screen_clear()

        
        while y not in paises_participantes_edicion_particular(z):

            screen_clear()

            print(f'\n\t2 - Cantidad de goles en una Copa Mundial a partir de un año y pais ingresado  \n\n')

            print(f"\tPaises participantes para el año: {z}\n")

            paises = paises_participantes_edicion_particular(z)

            imprimir_Lista_n_columnas(paises, 5 )

            y = input('\n\n\tIngrese un pais para consultar:\t')

               
        screen_clear()
            
        print(f"\n\n\tLa cantidad de goles de {y} en la edicion {z} fué {cantidad_goles_edicion_particular(y, z)} goles")

        input("\nPresione cualquier tecla para volver al menu")
       

    #---------------------------------------------------------------------------------------------------------------------
    elif x == '3':

        

        

        x = input()



    elif x == '4':
        print('---Consulta cuatro----')
        x = input()
    elif x == '5':
        print('---Consulta cinco----')
        x = input()
    else:
        break
    
