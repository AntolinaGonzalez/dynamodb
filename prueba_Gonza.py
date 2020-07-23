'''
from Funciones_Querys import *

x = input("\n\tIngrese un anio: \t")

#y = input("\n\n\tIngrese un anio: \t")


print()
print("\t INTEGRANTES DEL EQUIPO CAMPEON:  ", campeon_anio_particular(x))
print()
for jug in jugadores_equipo_campeon(x):

	print("\t\t", jug)

'''

cadena = 'rUns dOg' 

cadena = cadena.split()

cadena.reverse()

cadena_salida = []


for pal in cadena: 

	cadena_salida.append(pal.swapcase())

cadena_salida = " ".join(cadena_salida)
print(cadena_salida)


