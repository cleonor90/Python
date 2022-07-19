#Diseñe un programa que lea un número entero del intervalo de 1 a 4,
#correspondiente al estado civil de una persona, y determine el nombre del
#estado civil. Considere: 1 para soltero, 2 para casado, 3 para viudo y 4 para
#divorciado.

#Ingreso de datos
numero=int(input("Ingrese un numero del 1 al 4: "))

#Proceso de datos
if numero<1 or numero>4:
    mensaje= "Numero invalido"
if numero==1:
    mensaje= "Soltero"
if numero==2:
    mensaje="Casado"
if numero==3:
    mensaje="Viudo"
if numero==4:
    mensaje="Divorciado"

#Imprimir los datos
print ("Su estado civil es " + (mensaje))