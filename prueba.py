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

x=int(input('Ingrese un anio'))

for data in datosCups:
    if data['Year']== x:
        winner = data['Winner']
        second = data['Runners-Up']
        
f
