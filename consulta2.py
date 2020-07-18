from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key

#arreglar buscar primero la cantidad maxima

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")


cupTable = dynamodb.Table('WorldCup')
responseCup = cupTable.scan()

max=-9999
lista=[]
datos = responseCup['Items']

for data in datos:
    if data['GoalsScored']>= max:
        lista.append(str(data['GoalsScored']) +" "+ data['Winner'] + " " + str(data['Year']))
        

print(lista)