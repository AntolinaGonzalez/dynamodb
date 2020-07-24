from Funciones_Querys import *




arbitros = dict()

salida = [' ', 0]

for dato in datosMatches:

	if dato['Referee'] in arbitros.keys():

		arbitros[dato['Referee']] +=1

		if salida[1] < arbitros[dato['Referee']]:

			salida[0] = dato['Referee'] 
			salida[1] = arbitros[dato['Referee']]

	else: 

		arbitros[dato['Referee']] = 1


print(f'El arbitro {salida[0]} fue el que mas partidos dirigió con un total de: {salida[1]} partidos')





















