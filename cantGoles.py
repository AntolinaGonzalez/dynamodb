from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key

#Pais con mas cantidad de goles hasta el mundial del 98

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

matchesTable = dynamodb.Table('WorldMatches')
