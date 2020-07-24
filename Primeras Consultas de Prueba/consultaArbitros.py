
import boto3
from Funciones_Querys import * 
dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

#Devuelve el arbitro que referencio la mayor cantidad de partidos

arbitros=[]
arbitrosFinal=[]


for data in datosMatches:
    if data['Referee'] not in arbitros:
        arbitros.append(data['Referee'])

print(arbitros)

cantidadPartidosArbitrados=[0]*len(arbitros)

print (cantidadPartidosArbitrados)


for i in range(len(arbitros)-1):
    for data in datosMatches:
        if data['Referee']== arbitros[i]:
            cantidadPartidosArbitrados[i]= cantidadPartidosArbitrados[i] + 1

x= cantidadPartidosArbitrados.index(max(cantidadPartidosArbitrados))

print(f"El arbitro {arbitros[x]} es el que mas partidos dirigió, con un total de:  {cantidadPartidosArbitrados}")

