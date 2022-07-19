#Diseñe un programa que determine el mayor de 3 números enteros diferentes.

#Ingreso de datos
numero_1 = int(input("Ingresa el primer número : "))
numero_2 = int(input("Ingresa el segundo número : "))
numero_3 = int(input("Ingresa el tercer número : "))

#proceso
mayor=numero_1
if numero_2>mayor:
    mayor= numero_2
if numero_3>mayor:
    mayor=numero_3

#mostrar los resultados

print("El numero mayor es: " +str (mayor) )

