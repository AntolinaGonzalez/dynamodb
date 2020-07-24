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


    if x == '1':

        Contulta_1()

    elif x == '2':

        consulta_2()
       
    elif x == '3':

        consulta_3()
          
    elif x == '4':

        consulta_4()
        
    elif x == '5':
        
        consulta_5()
    
    else:
        portada()
        input("\n\n\t\t\tPresione cualquier tecla para cerrar....")
        break
    
