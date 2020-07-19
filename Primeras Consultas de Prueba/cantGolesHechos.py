from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key


dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

matchesTable = dynamodb.Table('WorldMatches')
responseMatches = matchesTable.scan()

year = 1986
cont = 0
datos = responseMatches['Items']

for data in datos:
    if data['Year']== year:
        if data['Home Team Initials']== "ARG":
            cont = cont + data['Home Team Goals']
        elif data['Away Team Initials']== "ARG":
            cont = cont + data['Away Team Goals']
print(cont)