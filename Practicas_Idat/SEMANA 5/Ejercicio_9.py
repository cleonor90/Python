#Ingreso de datos


sexo= int(input("Ingrese el sexo , Femenino(1), Masculino(2)"))
edad= int(input("ingrese su edad , si es mayor a 23 (1), si es menor (2)"))


#Proceso de datos
if sexo==1>23:
    sexo="FA"

else:
    sexo==1<23
    sexo="FB"

if sexo==2>25:
    sexo="MA"

else:
    sexo==2>25
    sexo="MB"

#Resultados
print("La categoria del postulante es: ", str(sexo))
