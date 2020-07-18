import boto3


def create_players_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.create_table(
        TableName='WorldPlayers',
        KeySchema=[
            {
                'AttributeName': 'Player Name',
                'KeyType': 'HASH'  # Partition key
            },

            {
                'AttributeName': 'MatchID', 
                'KeyType': 'RANGE' # Sort Key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'Player Name',
                'AttributeType': 'S'
            },

            {
                'AttributeName': 'MatchID', 
                'AttributeType': 'N'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )
    return table


if __name__ == '__main__':
    players_table = create_players_table()
    print("Estado de la tabla:", players_table.table_status)
