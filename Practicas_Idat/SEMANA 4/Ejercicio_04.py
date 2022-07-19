#Diseñe un programa que determine la categoría de un estudiante en base a su
#promedio ponderado, de acuerdo a la siguiente tabla:


#Ingreso de datos

promedio = float(input("Promedio: "))

#Proceso
if promedio>=17:
    categoria = "A"

if promedio>=14 and promedio<17:
    categoria = "B"

if promedio>=12 and promedio<14:
    categoria = "C"
    
if promedio>12:
    categoria ="D"

#Mostrar resultados

print("Categoria: " + categoria)  #Como es texto no agrega "str"
