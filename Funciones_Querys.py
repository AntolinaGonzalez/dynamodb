from pprint import pprint
from os import system, name
from time import sleep
import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

matchesTable = dynamodb.Table('WorldMatches')
playersTable = dynamodb.Table('WorldPlayers')
playersTableFinal = dynamodb.Table('WorldPlayersFinal')
cupsTable = dynamodb.Table('WorldCup')

responseMatches = matchesTable.scan()
responsePlayers = playersTable.scan()
responsePlayersFinal = playersTableFinal.scan()
responseCups = cupsTable.scan()

datosMatches = responseMatches['Items']
datosPlayers = responsePlayers['Items']
datosPlayersFinal = responsePlayersFinal['Items']
datosCups = responseCups['Items']

ediciones = (1930,1934,1938,1950,1954,1958,1962,1966,1970,1974,1978,1982,1986,1990,1994,1998,2002,2006,2010,2014)


#------------------------------------------------------------------------------------------------

def screen_clear():
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear')

#------------------------------------------------------------------------------------------------

def menuOpciones():

    print('\t+----------------------------------------------------------------------------------+')
    print('\t|                                Menú de opciones                                  |')
    print('\t+----------------------------------------------------------------------------------+')
    print('\t|                                                                                  |')
    print('\t| 1 - Paises participantes de la Copa Mundial a partir de un año ingresado         |')
    print('\t|                                                                                  |')
    print('\t| 2 - Cantidad de goles en una Copa Mundial a partir de un año y pais ingresado    |')
    print('\t|                                                                                  |')
    print('\t| 3 - Datos final de copa segun año: Estadio, Campeon, subcampeon y planteles      |')
    print('\t|                                                                                  |')
    print('\t| 4 - Consulta cuatro                                                              |')
    print('\t|                                                                                  |')
    print('\t| 5 - Consulta cinco                                                               |')
    print('\t|                                                                                  |')
    print('\t| 0 - Salir                                                                        |')
    print('\t+----------------------------------------------------------------------------------+')

#------------------------------------------------------------------------------------------------

def portada():

    print('\t+----------------------------------------------------------------------------------+')
    print('\t|                          Trabajo Final - Gestión de Datos                        |')
    print('\t|   UTN-Frre                    Gestor: DynamoDB Amazon                  año 2020  |')
    print('\t+----------------------------------------------------------------------------------+')
    print('\t|                                                                                  |')
    print('\t|            Grupo 1                                                               |')
    print('\t|                                                             Docentes             |')
    print('\t|-------> Badaró, Maximiliano                                                      |')
    print('\t|-------> Cao, Luis Gonzalo                          * Orcola, Carolina <----------|')
    print('\t|-------> Gonzalez, Antolina                         * Fernandez, Juan Carlos <----|')
    print('\t|-------> Mambrin Ventre, Jonathan                   * Romero, Leandro  <----------|')
    print('\t|-------> Rolón, Tomás                                                             |')
    print('\t+----------------------------------------------------------------------------------+')
    
    input()

#------------------------------------------------------------------------------------------------

def es_anio(anio):

	#Parametro 'anio' un año correspondiente a una edicion de la copa del tipo int() 
	#Retorna True/False si es o no un anio en el que se jugo una copa del mundo.

	if int(anio) in ediciones:

		return True

	return False

#------------------------------------------------------------------------------------------------

def paises_participantes():

	#Retorna una lista con los nombres de los paises que participaron de alguna edicion de la copa.

	salida = list()

	for data in datosMatches:
		if data['Home Team Name'] not in salida:	
			salida.append(data['Home Team Name'])
		
		if data['Away Team Name'] not in salida:
			salida.append(data['Away Team Name'])

	return salida
#-------------------------------------------------------------------------------------------------

def es_pais(pais):

	#Parametro 'pais' el nombre del pais en ingles ej:('Argentina', 'Brazil', 'France') del tipo str()
	#Retorna True/False si es o no un pais que participo de algun mundial

	if pais in paises_participantes():

		return True

	return False

#------------------------------------------------------------------------------------------------

def paises_participantes_edicion_particular(anio):

	##Parametro 'anio' un año correspondiente a una edicion de la copa del tipo int() 
	#Retorna una lista con los nombres de los paises participantes de todas las ediciones.

	if es_anio(anio):

		salida = list()

		for data in datosMatches:

			if data['Year'] == int(anio):
				
				if data['Home Team Name'] not in salida:	
					salida.append(data['Home Team Name'])
				
				elif data['Away Team Name'] not in salida:
					salida.append(data['Away Team Name'])

		return salida


#------------------------------------------------------------------------------------------------

def paises_participantes_todas_ediciones():

	#Retorna una lista con los nombres de los paises participantes de todas las ediciones.

	lista = list()
	no_participo = list()
	for match in datosMatches: 
		for edicion in ediciones: 
			participantes = paises_participantes_edicion_particular(edicion)

			if match['Home Team Name'] not in participantes: 
				no_participo.append(match['Home Team Name'])
			elif match['Away Team Name'] not in participantes: 
				no_participo.append(match['Away Team Name'])
				
	for match in datosMatches: 
		if match['Home Team Name'] not in lista and match['Home Team Name'] not in no_participo: 
			lista.append(match['Home Team Name'])
		elif match['Away Team Name'] not in lista and match['Away Team Name'] not in no_participo: 
			lista.append(match['Away Team Name'])

	return lista





#-----------------------------------------------------------------------------------


def es_pais_edicion_particular(pais, anio):

	#Parametro 'pais' el nombre del pais en ingles ej:('Argentina', 'Brazil', 'France') del tipo str()
	#Parametro 'anio' un año correspondiente a una edicion de la copa del tipo int() 
	#Retorna True/False si es o no un pais que participo de la edicion solicitada

	if pais in paises_participantes():

		if es_anio(anio):

			for data in datosMatches:

				if data['Year'] == int(anio):

					if pais in paises_participantes_edicion_particular(anio):

						return True
	return False
	

#-------------------------------------------------------------------------------------------------

def cantidad_partidos(pais, anio):

	#Parametro 'pais' el nombre del pais en ingles ej:('Argentina', 'Brazil', 'France') del tipo str()
	#Parametro 'anio' un año correspondiente a una edicion de la copa del tipo int() 
	#Retorna la cantidad de partidos que disputo dicha seleccion. 
	
	if es_pais(pais) and es_anio(anio):

		cont = 0

		for data in datosMatches:
			if data['Year'] == int(anio):
				if data['Home Team Name']== pais or data['Away Team Name']== pais:
					cont += 1
		return cont

#------------------------------------------------------------------------------------------------

def cantidad_partidos_total(pais):

	#Parametro 'pais' el nombre del pais en ingles ej:('Argentina', 'Brazil', 'France') del tipo str()
	#Retorna la cantidad de partidos que disputo dicha seleccion en todas las ediciones de la copa. 

	if es_pais(pais):

		cont = 0
		
		lista = list(ediciones)

		for data in datosMatches:
			
			if data['Home Team Name'] == pais or data['Away Team Name'] == pais:
				
				cont += 1
		
		return cont

#-----------------------------------------------------------------------------------------------

def cantidad_goles_edicion_particular(pais, anio):

	#Parametro 'pais' el nombre del pais en ingles ej:('Argentina', 'Brazil', 'France') del tipo str()
	#Parametro 'anio' un año correspondiente a una edicion de la copa del tipo int() 
	#Retorna la cantidad de goles que convirtio dicha seleccion en el torneo ingresado como anio. 
	
	

	if es_pais(pais) and es_anio(anio):

		cont = 0

		for data in datosMatches:
			
			if data['Year']== int(anio):
				
				if data['Home Team Name']== pais:
					
					cont = cont + data['Home Team Goals']
			   
				elif data['Away Team Name']== pais:
					
					cont = cont + data['Away Team Goals']
		return cont



#------------------------------------------------------------------------------------------------

def cantidad_goles_total(pais):

	#Parametro 'pais' el nombre del pais en ingles ej:('Argentina', 'Brazil', 'France') del tipo str()
	#Parametro 'anio' un año correspondiente a una edicion de la copa del tipo int() 
	#Retorna la cantidad total de goles que convirtio dicha seleccion en todas las ediciones.
	

	if es_pais(pais):

		cont = 0

		for data in datosMatches:
				
			if data['Home Team Name']== pais:
			
				cont = cont + data['Home Team Goals']
			   
			elif data['Away Team Name']== pais:
			
				cont = cont + data['Away Team Goals']
		
		return cont


#------------------------------------------------------------------------------------------------

def cantidad_campeonatos(pais):

	#Parametro 'pais' el nombre del pais en ingles ej:('Argentina', 'Brazil', 'France') del tipo str()
	#Retorna la cantidad de copas ganadas por dicha seleccion.

	if es_pais(pais):

		cont = 0

		for data in datosCups:

			if data['Winner'] == pais:

				cont += 1

		return cont

#---------------------------------------------------------------------------------------------------

def datos_final(anio):

	#Parametro 'anio' un año correspondiente a una edicion de la copa del tipo int() 
	#Retorna una lista[matchid, estadio, winner, winner initials , second, second initials ] 

	salida = []

	for data in datosMatches:

		if data['Year'] == int(anio) and data['Stage'] == "Final":


			salida.append(data['MatchID'])
			salida.append(data['Stadium'])

			if data['Home Team Goals'] > data['Away Team Goals']:
				
				salida.append(data['Home Team Name'])
				salida.append(data['Home Team Initials'])
				salida.append(data['Away Team Name'])
				salida.append(data['Away Team Initials'])
			else: 
				salida.append(data['Away Team Name'])
				salida.append(data['Away Team Initials'])
				salida.append(data['Home Team Name'])
				salida.append(data['Home Team Initials'])
	
	return salida


#---------------------------------------------

def goles_recibidos_edicion_particular(pais, anio): 

	#Parametro 'pais' el nombre del pais en ingles ej:('Argentina', 'Brazil', 'France') del tipo str()
	#Parametro 'anio' un año correspondiente a una edicion de la copa del tipo int() 
	#Retorna la cantidad de goles que convirtio dicha seleccion en el torneo ingresado como anio.

	if es_pais(pais) and es_anio(anio):

		cont = 0

		for data in datosMatches:
			
			if data['Year']== int(anio):
				
				if data['Home Team Name']== pais:
					
					cont = cont + data['Away Team Goals']
			   
				elif data['Away Team Name']== pais:
					
					cont = cont + data['Home Team Goals']
		return cont

#-----------------------------------------------------------------

def campeones():  

	#Retorna una lista con todos los campeones de los mundiales y el año en que ganaron

	salida = list()

	for data in datosCups: 

		salida.append(data['Winner'], data['Year'])

	return salida

#--------------------------------------------------------------


def es_campeon(pais): 

	#Retorna verdadero si el país especificado fue campeon alguna vez en algún mundial

	campeones_n = []

	for campeon in campeones(): 

		campeones_n.append(campeon[0])


	if pais in campeones_n: 
		return True
	return False

#--------------------------------------------------------------

def campeon_anio_particular(anio): 

	if es_anio(anio): 

		for cup in datosCups: 

			if cup['Year'] == int(anio): 

				return cup['Winner']

#-------------------------------------------------------------

def datos_paises(): 

	salida = dict()

	for edicion in ediciones: 

		anio = str(edicion)

		nombre = campeon_anio_particular(anio)

		salida[edicion] = (nombre, int(cantidad_goles_edicion_particular(nombre, anio)), int(goles_recibidos_edicion_particular(nombre,anio)))

	return salida



#---------------------------------------------------------------------------------------------------------------------

def campeon_con_max_dif_goles(): 

	paises = datos_paises()

	maximo = paises[1930][1] - paises[1930][2]

	salida = [paises[1930][0], maximo,1930]

	for edicion in ediciones: 

		diferencia = paises[edicion][1] - paises[edicion][2]

		if diferencia > maximo: 

			maximo = diferencia 
			salida = [paises[edicion][0], maximo, edicion]

	return salida


#------------------------------------------------------------------------------------------------------------------------

def campeon_con_min_dif_goles(): 

	paises = datos_paises()

	minimo = paises[1930][1] - paises[1930][2]

	salida = [paises[1930][0], minimo,1930]

	for edicion in ediciones: 

		diferencia = paises[edicion][1] - paises[edicion][2]

		if diferencia < minimo: 

			minimo = diferencia 
			salida = [paises[edicion][0], minimo, edicion]

	return salida

#------------------------------------------------------------------------------------------------------------------------


def jugadores_equipo_campeon(anio):

	#Retorna una lista() con los nombres de los jugadores que participaron en el torneo para dicho equipo,
	#Anda bien con los anios: 1930, 1934, 1938, 1970, 1986 

	datos = datos_final(anio)

	matchid = datos[0]

	pais = datos[3]
	
	salida = list()

	for jugador in datosPlayersFinal:

		if jugador['MatchID'] == matchid:

			if jugador['Team Initials'] == pais:

				salida.append(jugador['Player Name'])

	return salida 

#--------------------------------------------------------------------------------------------------------------

def jugadores_equipo_subcampeon(anio):

	#Retorna una lista[matchid, estadio, winner, winner initials , second, second initials ] 

	#Retorna una lista() con los nombres de los jugadores que participaron en el torneo para dicho equipo,
	#Anda bien con los anios: 1930, 1934, 1938, 1970, 1986 

	datos = datos_final(anio)

	matchid = datos[0]

	pais = datos[5]
	
	salida = list()

	for jugador in datosPlayersFinal:

		if jugador['MatchID'] == matchid:

			if jugador['Team Initials'] == pais:

				salida.append(jugador['Player Name'])

	return salida 


#--------------------------------------------------------------------------------------------------------------

def imprimir_Lista_1_columna(unaLista):

	#Recibe como parametro una lista()
	#Imprime en una columna todos los datos

	for i in range(len(unaLista)):

		print(f'\t{unaLista[i]}')

#--------------------------------------------------------------------------------------------------------------

def imprimir_Lista_n_columnas(unaLista, n ):

	#Recibe como parametro una lista() y un numero entero
	#Imprime los datos en n columnas 

	cont = 0

	for i in range((len(unaLista) // n )+1): 
		print()
		for j in range(n):
			if cont == len(unaLista):
				break
			else: 
				print("|  ", unaLista[cont], end=' |')
				cont += 1  


