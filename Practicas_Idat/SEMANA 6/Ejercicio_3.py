#ingreso de datos
velocidad=float(input("Ingrese su velocidad: "))

#Proceso de datos
if velocidad<=70:
    multa="Sin sanción"

elif velocidad<=90:
    multa="Su multa son S/.100 "

elif velocidad<=100:
    multa="Su multa son S/.140 "

else:
    velocidad>100
    multa="Su multa es S/.200 "

print("Su multa es: " + multa)
