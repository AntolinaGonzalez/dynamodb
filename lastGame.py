from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key

#En que estadio fue el ultimo partido donde se decidieron los ganadores de un anio en cuestion

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

matchesTable = dynamodb.Table('WorldMatches')
cupTable = dynamodb.Table('WorldCup')

responseMatches = matchesTable.scan()
responseCup = cupTable.scan()

datosMatches = responseMatches['Items']
datosCup = responseCup['Items']

year = 1978

for data in datosCup:
    if data['Year']==year:
        winner = data['Winner']
        second = data['Runners-Up']

print('The Winner is ' + winner)
print('The Runners-up is '+ second)

for data in datosMatches:
    if data['Home Team Name'] == winner and data['Year']== year and data['Away Team Name']==second:
        stadio= data['Stadium']
print(stadio)