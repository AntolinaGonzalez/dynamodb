from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key


dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

matchesTable = dynamodb.Table('WorldMatches')
#playerTable = dynamodb.Table('WorldPlayers')
#cupTable = dynamodb.Table('WorldCup')

responseMatches = matchesTable.scan()
#responsePlayer = playerTable.scan()
#responseCup = cupTable.scan()
year = 1986
cont = 0
datos = responseMatches['Items']
#response = table.scan()
#data2 = response['Items']
#devuelve toda la tabla
#table1 = dynamodb.Table('MoviesSecond')
#response1 = table1.scan()
#data1 = response1['Items']
#data1 = response1['LastEvaluatedKey'] -- no funciona
#data = response['Items'] + response1['Items']
# if response['Items']['year']== response1['Items']['year']:
#     respuesta.append(response['Items']['year'])
#data = response['Count'] + response1['Count'] cuenta la cantidad de items
# for datos in data1:
#     respuesta.append(datos['title'])
# for datos in data2:
#     respuesta1.append(datos['title'])
# for i in range(len(respuesta1)):
#     for j in range(len(respuesta)):
#         if respuesta[j]== respuesta1[i]:
#             resultado.append(respuesta[j])
# print(resultado)
for data in datos:
    if data['Year']== year:
        if data['Home Team Initials']== "ARG" or data['Away Team Initials']== "ARG":
            cont = cont +1
print(cont)