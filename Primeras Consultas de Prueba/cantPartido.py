from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key

#arreglar buscar primero la cantidad maxima

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

matchesTable = dynamodb.Table('WorldMatches')
responseMatches = matchesTable.scan()
lista= [1930,1934,1938,1950,1954,1958,1962,1966,1970,1974,1978,1982,1986,1990,1994,1998,2002,2006,2010,2014]
datos = responseMatches['Items']
cont = 0

for data in datos:
    if data['Year'] in lista and (data['Home Team Name'] == "Brazil"  or data['Away Team Name']=="Brazil"):
        cont =  cont +1
        lista.remove(data['Year'])
        
print(cont)