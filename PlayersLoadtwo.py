from decimal import Decimal
import json
import boto3


def load_players(players, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('WorldPlayersTwo')
    for player in players:
        name = player['Player Name']
        match_ID = player['MatchID']
        team = player['Team Initials']
        shirt = player['Shirt Number']

        print("Adding player: {} | {} | {} | {}".format(match_ID , name, shirt, team))
        table.put_item(Item=player)


if __name__ == '__main__':
    with open("WorldCupPlayers.json") as json_file:
        players_list = json.load(json_file, parse_float=Decimal)
    load_players(players_list)
