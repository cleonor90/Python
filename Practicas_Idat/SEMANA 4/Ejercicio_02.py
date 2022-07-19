#Dado un partido de fútbol jugado entre dos equipos A y B, diseñe un programa
#que determine el resultado del partido entre ganó A, ganó B o hubo empate

#Ingreso de datos
GolesEquipoA = int(input("Goles del equipo \"A\" :"))
GolesEquipoB = int(input("Goles del equipo \"B\" :"))

#Proceso

if GolesEquipoA>GolesEquipoB:
    resultado= "Gano el equipo \"A\""

if GolesEquipoB>GolesEquipoA:
    resultado= "Gano el equipo \"B\""

if GolesEquipoA==GolesEquipoB:
    resultado= "Empate"

print(resultado) 
