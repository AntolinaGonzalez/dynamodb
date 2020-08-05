from decimal import Decimal
import json
import boto3


def load_matches(matches, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('WorldMatches1')
    for match in matches:
        year = match['Year']
        local = match['Home Team Name']
        away = match['Away Team Name']

        print("Adding match: {} vs {} in {}".format(local,away,year))
        table.put_item(Item=match)


if __name__ == '__main__':
    with open("../WorldCupMatches.json") as json_file:
        matches_list = json.load(json_file, parse_float=Decimal)
    load_matches(matches_list)
