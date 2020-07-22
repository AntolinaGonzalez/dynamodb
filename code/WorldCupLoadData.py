from decimal import Decimal
import json
import boto3


def load_fifa_cup(world_cups, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('WorldCup')
    for cup in world_cups:
        year = cup['Year']
        country = cup['Country']
        winner = cup['Winner']

        print("Adding cup: ", year, country, winner)
        table.put_item(Item=cup)


if __name__ == '__main__':
    with open("../WorldCup.json") as json_file:
        cup_list = json.load(json_file, parse_float=Decimal)
    load_fifa_cup(cup_list)
