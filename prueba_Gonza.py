from Funciones_Querys import *

x = input("\n\tIngrese un anio: \t")

#y = input("\n\n\tIngrese un anio: \t")


print()
print("\t INTEGRANTES DEL EQUIPO CAMPEON:  ", campeon_anio_particular(x))
print()
for jug in jugadores_equipo_campeon(x):

	print("\t\t", jug)


