from Funciones_Querys import *


for jug in datosPlayers: 
	if jug['Team Initials'] == "ARG": 
		if jug['MatchID'] <= 2198: 
			print(jug['MatchID'])
