import boto3


def create_matches_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.create_table(
        TableName='WorldMatches1',
        KeySchema=[
            {
                'AttributeName': 'MatchID',
                'KeyType': 'HASH'  # Partition key
            },

            {
                'AttributeName': 'Year', 
                'KeyType': 'RANGE' # Sort Key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'Year',
                'AttributeType': 'N'
            },

            {
                'AttributeName': 'MatchID', 
                'AttributeType': 'N'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    return table


if __name__ == '__main__':
    world_matches_table = create_matches_table()
    print("Estado de la tabla:", world_matches_table.table_status)
