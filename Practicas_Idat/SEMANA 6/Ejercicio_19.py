#Ingreso de datos

numero = int(input("Ingrese una cifra de 4 digitos: "))

#Proceso

millar = numero // 1000
centena = numero // 100%10
decena = numero // 10%10
unidad = numero % 10 

if millar == 1:
    estado = "Soltero"
elif millar ==2:
    estado = "Casado"
elif millar == 3:
    estado = "Viudo"
elif millar ==4:
    estado = "Casado"
else:
    "NÚMERO INGRESADO INVALIDO"

edad = (str(centena) +str(decena))

if unidad == 1:
    sexo = "Masculino"
elif unidad ==2:
    sexo = "Femenino"
else:
    "NÚMERO INGRESADO INVALIDO"