#Ingreso de datos
Numero=int(input("Ingrese el número entero del 1 al 7: "))

#Proceso
if Numero==1:
    nombre="Lunes"
elif Numero==2:
    nombre="Martes"
elif Numero==3:
    nombre="Miercoles"
elif Numero==4:
    nombre="Jueves"
elif Numero==5:
    nombre="Viernes"
elif Numero==6:
    nombre="Sabado"
elif Numero==7:
    nombre="Domingo"



#Resultados
print("El nombre del día: " + str(nombre))