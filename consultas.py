from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

matchesTable = dynamodb.Table('WorldMatches')
playersTable = dynamodb.Table('WorldPlayers')
cupsTable = dynamodb.Table('WorldCup')
finalPlayersTable = dynamodb.Table('WorldPlayersFinal')


def datos_segun_edicion(unAnio): 
	responseCups = cupsTable.get_item(Key = {'Year':unAnio})

	return responseCups['Item']


def jugadores_argentina_final(): 
	
	responsePlayers = finalPlayersTable.scan(
	    FilterExpression = Attr('Team Initials').eq("ARG")
	)

	datosPlayers = responsePlayers['Items']

	for i in datosPlayers: 
	    print(i['Player Name'])


def estadio_final(unAnio): 

	responseMatch = matchesTable.scan(
		FilterExpression = Attr('Stage').eq('Final') & Attr('Year').eq(unAnio)
	)

	datos = responseMatch['Items']

	return datos[0]['Stadium']



def estadios_maradona():
	responsePlayers = playersTable.scan(
		FilterExpression = Attr('Player Name').eq('Diego MARADONA')
	)

	datos = responsePlayers['Items']

	matchIDs = list()

	for i in datos: 
		matchIDs.append(i['MatchID'])



	datos_maradona = list()

	for i in matchIDs: 
		responseMatch = matchesTable.scan(
			FilterExpression = Attr('MatchID').eq(i)
		)

		d = responseMatch['Items']

		datos_maradona = datos_maradona + d 


	for i in datos_maradona: 
		print(i['Stadium'])



estadios_maradona()