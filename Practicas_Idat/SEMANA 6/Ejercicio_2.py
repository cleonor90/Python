#Ingreso de datos
promedio_ponderado= float(input("Ingrese promedio ponderado: "))

#Proceso
if promedio_ponderado>=17:
    categoria="A"
elif promedio_ponderado>=14:
    categoria="B"
elif promedio_ponderado>=12:
    categoria="C"
else:
    categoria="D"

print("Categoria: " + categoria)