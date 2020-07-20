from pprint import pprint
import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

matchesTable = dynamodb.Table('WorldMatches')
playersTable = dynamodb.Table('WorldPlayers')
cupsTable = dynamodb.Table('WorldCup')

responseMatches = matchesTable.scan()
responsePlayers = playersTable.scan()
responseCups = cupsTable.scan()

datosMatches = responseMatches['Items']
datosPlayers = responsePlayers['Items']
datosCups = responseCups['Items']

ediciones = (1930,1934,1938,1950,1954,1958,1962,1966,1970,1974,1978,1982,1986,1990,1994,1998,2002,2006,2010,2014)

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
	#Retorna una lista[matchid, estadio, winner, second] 

	salida = []

	for data in datosMatches:

		if data['Year'] == int(anio) and data['Stage'] == "Final":


			salida.append(int(data['MatchID']))
			salida.append(data['Stadium'])

			if data['Home Team Goals'] > data['Away Team Goals']:
				
				salida.append(data['Home Team Name'])
				salida.append(data['Away Team Name'])
			else: 
				salida.append(data['Away Team Name'])
				salida.append(data['Home Team Name'])
	
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

			if cup['Year'] == anio: 

				return cup['Winner']

	else: 
		print("Ese año no corresponde")








#-------------------------------------------------------------

def datos_paises(): 

	salida = dict()

	for edicion in ediciones: 

		anio = str(edicion)
		nombre = campeon_anio_particular(anio)

		salida[edicion] = (nombre, cantidad_goles_edicion_particular(nombre, anio), goles_recibidos_edicion_particular(nombre,anio))


	return salida



#--------------------------------------------------------------








