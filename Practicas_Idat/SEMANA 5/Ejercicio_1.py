#En una autopista se multa a los conductores de vehículos que exceden el límite
#de velocidad permitido de acuerdo a la siguiente tabla.

velocidad= float(input("Ingrese la velocidad: "))

#Ingreso de datos

if velocidad<=0:
    mensaje= "Velocidad no valida"
if velocidad>=0 and velocidad <=70:
    mensaje= "No hay sanción"
if velocidad>70 and velocidad<=90:
    mensaje= "Multa de  de S.100.00 " 
if velocidad>90 and velocidad<=100:
    mensaje= "Multa de S.140.00"
if velocidad>100:
    mensaje= "Multa de S.200.00"

print ("Su multa es: " + (mensaje))
   

