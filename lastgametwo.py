from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key

#En que estadio fue el ultimo partido donde se decidieron los ganadores de un anio en cuestion

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
lista=[]
matchesTable = dynamodb.Table('WorldMatches')
cupTable = dynamodb.Table('WorldCup')
playerTable = dynamodb.Table('WorldPlayersTwo')

responseMatches = matchesTable.scan()
responseCup = cupTable.scan()
responsePlayers = playerTable.scan()

datosMatches = responseMatches['Items']
datosCup = responseCup['Items']
datosPlayer = responsePlayers['Items']


year = 1986

for data in datosCup:
    if data['Year']==year:
        winner = data['Winner']
        second = data['Runners-Up']
        

print('The Winner is ' + winner)
print('The Runners-up is '+ second)

for data in datosMatches:
    if (data['Home Team Name'] == winner or data['Away Team Name'] == winner) and data['Year']== year and (data['Away Team Name']==second or data['Home Team Name'] == second):
        matchId= data['MatchID']
        stadio= data['Stadium']
    if data['Home Team Name'] == winner:
        initialswinner= data['Home Team Initials']
    if data['Away Team Name'] == winner:
        initialswinner= data['Away Team Initials']
    if data['Home Team Name'] == second:
        initialsSecond= data['Home Team Initials']
    if data['Away Team Name'] == second:
        initialsSecond = data['Away Team Initials']

lista=[]
print(stadio)
print(matchId)
print()  
print("Jugadores de " + winner)
print()
for data in datosPlayer:
    if data['Team Initials']==initialswinner and data['MatchID']==matchId:
        print(data['Player Name'])
print()   
print("Jugadores de " + second)
print()
for data in datosPlayer:
    if data['Team Initials']==initialsSecond and data['MatchID']==matchId:
        print(data['Player Name'])
        





