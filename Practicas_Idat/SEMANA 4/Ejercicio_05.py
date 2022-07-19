#Un estudiante recibe una propina de S/.100. El estudiante rinde tres exámenes
#(matemática, lenguaje e historia). Su padre ha decidido incentivarlo dándole una
#propina adicional de S/. 20 por cada examen aprobado (la nota mínima
#aprobatoria es 13). Diseñe un programa que determine el monto total de la
#propina que le corresponde al estudiante.

#Ingreso de datos
matematica =int(input("Matematicas: "))
lenguaje=int(input("Lenguaje: "))
Historia=int(input("historia: "))

#Proceso
propina=100
if matematica>=13:
    propina +=20 #propina = propina + 20

if lenguaje>=13:
    propina+=20 #propina = propina + 20

if Historia>=13:
    propina+=20

#Mostrar resultados

print("propina: " + str(propina))
