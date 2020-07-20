from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key

#Pais con mas cantidad de goles hasta el mundial del 2014

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

matchesTable = dynamodb.Table('WorldMatches')
responseMatches = matchesTable.scan()
datosMatches = responseMatches['Items']
paises = []

for data in datosMatches:
    paises.append(data['Home Team Name'])
    paises.append(data['Away Team Name'])

paises =  list(set(paises))

#print(paises)
cant = []
for i in range(len(paises)):
    contador = 0
    for data in datosMatches:
        if paises[i]==data['Home Team Name'] or paises[i]==data['Away Team Name']:
            contador = contador + 1
    cant.append(contador)
maxima = -9999

for i in range(len(cant)):
    if maxima < cant[i]:
        maxima = cant[i]
        pais = paises[i]
print(maxima)
print(pais)