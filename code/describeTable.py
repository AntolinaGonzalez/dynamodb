import boto3


def create_fifaCup_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.describe-table('WorldCup')
       
    return table


if __name__ == '__main__':
    world_cup_table = create_fifaCup_table()
    print("Estado de la tabla:", world_cup_table)
