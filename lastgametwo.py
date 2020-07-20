from pprint import pprint
import boto3

#En que estadio fue el ultimo partido donde se decidieron los ganadores de un anio en cuestion

'''
Lista los jugadores de cada equipo en la final de un año en particular
'''


dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
lista=[]
matchesTable = dynamodb.Table('WorldMatches')
cupTable = dynamodb.Table('WorldCup')
playerTable = dynamodb.Table('WorldPlayers')

responseMatches = matchesTable.scan()
responseCup = cupTable.scan()
responsePlayers = playerTable.scan()

datosMatches = responseMatches['Items']
datosCup = responseCup['Items']
datosPlayer = responsePlayers['Items']

year = 1986

for data in datosCup:
    if data['Year'] == year:
        winner = data['Winner']
        second = data['Runners-Up']
        break
        

print('The Winner is ' + winner)
print('The Runners-up is ' + second)

for data in datosMatches:
    if ((data['Home Team Name'] == winner and data['Away Team Name'] == second) or (data['Home Team Name'] == second and data['Away Team Name']== winner)) and (data['Year'] == year): 
        stadio = data['Stadium']
        matchId = data['MatchID']
        break


print(stadio)
print(matchId)
print("Jugadores de " + winner)

for data in datosPlayer:
    if data['Team Initials'] == "ARG": 
        print(data['Player Name'])
    




