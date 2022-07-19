#Diseñe un programa que determine el mayor de 3 números enteros diferentes.

#Ingreso de datos
numero_1 = int(input("Ingresa el primer número : "))
numero_2 = int(input("Ingresa el segundo número : "))
numero_3 = int(input("Ingresa el tercer número : "))


#Desarrollo
if numero_1 > numero_2 and numero_1 > numero_3:
    mensaje = "El primer número es el mayor"

if numero_2 > numero_1 and numero_2 > numero_3:
    mensaje = "El segundo número es el mayor"

if numero_3 > numero_2 and numero_3 > numero_1:
    mensaje = "El tercer número es el mayor"

#Impresión
print(mensaje)