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

table = dynamodb.Table('WorldPlayers')
response = table.scan(
    FilterExpression=Attr('RoundID').eq("201")
)

pprint(response)