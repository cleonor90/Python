#ingreso de datos
goles_a=int(input("Goles A: "))
goles_b=int(input("Goles B: "))

#Proceso

if goles_a>goles_b:
    resultado="Gano A"  #El programa evalua cada condición

elif goles_b>goles_a:
    resultado="Gano B"

else:
    resultado="Empate"

#Resultado
print(resultado)