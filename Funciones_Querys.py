from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

matchesTable = dynamodb.Table('WorldMatches')
playerTable = dynamodb.Table('WorldPlayers')
cupTable = dynamodb.Table('WorldCup')

responseMatches = matchesTable.scan()
responsePlayer = playerTable.scan()
responseCup = cupTable.scan()

ediciones = [1930,1934,1938,1950,1954,1958,1962,1966,1970,1974,1978,1982,1986,1990,1994,1998,2002,2006,2010,2014]


#-----------------------------------------------------------------------------------------------

def cantidad_partidos_pais_mundial(pais, anio):

	#Parametro 'pais' el nombre del pais ej:('Argentina', 'Brazil', 'Francia') del tipo str()
	#Parametro 'anio' un año correspondiente a una edicion de la copa del tipo int() 
	#Retorna la cantidad de partidos que disputo dicha seleccion. 
	
	datos = responseMatches['Items']
	
	cont = 0

	for data in datos:
	    if data['Year'] == anio:
	        if data['Home Team Name']== pais or data['Away Team Name']== pais:
	            cont += 1
	return cont

#------------------------------------------------------------------------------------------------

def cantidad_partidos_total_mundiales(pais):

	#Parametro 'pais' el nombre del pais ej:('Argentina', 'Brazil', 'Francia') del tipo str()
	#Retorna la cantidad de partidos que disputo dicha seleccion en todas las ediciones de la copa. 

	datos = responseMatches['Items']
	
	cont = 0
	
	lista = list(ediciones)

	for data in datos:
    if data['Year'] in lista and (data['Home Team Name'] == pais or data['Away Team Name'] == pais):
        cont += 1
        lista.remove(data['Year'])
        
	return cont

#-----------------------------------------------------------------------------------------------

def cantidad_goles_pais_anio(pais, anio):

	#Parametro 'pais' el nombre del pais ej:('Argentina', 'Brazil', 'Francia') del tipo str()
	#Parametro 'anio' un año correspondiente a una edicion de la copa del tipo int() 
	#Retorna la cantidad de partidos que disputo dicha seleccion. 
	
	datos = responseMatches['Items']

	cont = 0

	for data in datos:
	    
	    if data['Year']== anio:
	        
	        if data['Home Team Name']== pais:
	            
	            cont = cont + data['Home Team Goals']
	       
	        elif data['Away Team Name']== pais:
	            
	            cont = cont + data['Away Team Goals']
	return cont

#------------------------------------------------------------------------------------------------

def paises_participantes_todas_ediciones():

	#Retorna una lista con los nombres de los paises participantes de todas las ediciones.

	datos = responseMatches['Items']

	salida = list()

	for data in datos:
		if data['Home Team Name'] not in lista:	
			lista.append(data['Home Team Name'])
		
		elif data['Away Team Name'] not in lista:
			lista.append(data['Away Team Name'])

	return salida

#------------------------------------------------------------------------------------------------

