from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError


def get_movie(nombre, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('WorldPlayers')

    try:
        response = table.get_item(Attr={'MatchID':749,'Player Name': nombre})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']

dynamodb = None
if not dynamodb: 

    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

table = dynamodb.Table('WorldMatches')
responseMatch = table.scan(
    FilterExpression=Attr('Stage').eq("Final") & (Attr('Home Team Name').eq("Argentina") | Attr('Away Team Name').eq("Argentina"))
)

datos = responseMatch['Items']

tablePlayers = dynamodb.Table('WorldPlayersFinal')
responsePlayers = tablePlayers.scan(
    FilterExpression = Attr('Team Initials').eq("ARG")
)

datosPlayers = responsePlayers['Items']

for i in datosPlayers: 
    print(i['Player Name'])