import boto3

def delete_movie_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('WorldPlayersP1')
    table.delete()


if __name__ == '__main__':
    delete_movie_table()
    print("Players table deleted.")
