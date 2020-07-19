
import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
cupTable = dynamodb.Table('WorldCup')
response_cup = cupTable.scan()

cups = response_cup['Items']

x = input('\n\n\tIngrese un anio: \t')

for cup in cups: 
	if int(x) == cup['Year']: 
		print(cup['Winner'])
		break
