#Ingreso de datos
prestamo=float(input("Ingrese el monto del prestamo"))

#Proceso
if prestamo<=5000:
    cuotas=2

elif prestamo<=10000:
    cuotas=4

elif prestamo<=15000:
    cuotas=6

else:
    cuotas=10

if prestamo>10000:
    intereses=prestamo*3/100
else:
    intereses=prestamo*5/100

cuotaMensual=prestamo/cuotas + intereses
interesTotal=intereses*cuotas

#Mostrar resultados
print("numero de cuotas " + str(cuotas))
print("Cuota Mensual: "+str(cuotaMensual))
print("Interes total: "+str(interesTotal))