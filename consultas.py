from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

matchesTable = dynamodb.Table('WorldMatches')
playersTable = dynamodb.Table('WorldPlayers')
cupsTable = dynamodb.Table('WorldCup')

responseMatches = matchesTable.scan()
responsePlayers = playersTable.scan()
responseCups = cupsTable.scan()


responseMatches = matchesTable.scan(
    FilterExpression=Attr('Year').eq(1930)
)
items = responseMatches['Items']
print(items)