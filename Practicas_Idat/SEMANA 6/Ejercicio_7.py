#Ingreso de datos
from glob import escape


peso=float(input("Ingrese su peso: "))
estatura=(float(input("Ingrese su estatura: ")))

#Proceso de datos

imc=peso/(estatura*estatura)
if imc<20:
    grado="delgado"
elif imc>=20 and imc<25:
    grado="Normal"
elif imc>=25 and imc<30:
    grado="Sobrepeso"
elif imc>=30:
    grado="obesidad"

#Muestra los resultados

print("Su grado de obesidad es: "+ str(grado))