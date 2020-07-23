from Funciones_Querys import *

#Retorna una lista[matchid, estadio, winner, winner initials , second, second initials ] 



x = input('\tIngrese un anio: ')

datos = datos_final(x)


print('\n--------------------------------------------------------------------------')
print(f'\n\tEstadio donde se disputó la final: {datos[1]}            año {x}')
print('----------------------------------------------------------------------------')
print("\n\tCampeón:  " + datos[2] + "\n\n")

for data in datosPlayersFinal:

    if datos[0] == data['MatchID'] and datos[3] == data['Team Initials']:
        
        print("\t" + data['Player Name'])

print('----------------------------------------------------------------------------')
print("\n\tSubcampeón:  " + datos[4] + "\n\n")

for data in datosPlayersFinal:

    if datos[0] == data['MatchID'] and datos[5] == data['Team Initials']:
        
        print("\t" + data['Player Name'])






