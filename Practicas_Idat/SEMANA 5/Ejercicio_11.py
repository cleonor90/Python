#Ingreso de datos
numero =int(input("Ingrese un # de 3 cifras "))


if numero>=100 and numero<=999:
    centena= numero//100
    decena=numero//10%10
    unidad=numero%10

#123 cifra consecutiva
if (centena==decena-1 and decena==unidad-1) or (centena==decena+1 and decena==unidad+1):
    mensaje= "Cifras consecutivas"
else:
    mensaje= "Cifras No consecutivas"


#Mostrar resultado
print(mensaje)