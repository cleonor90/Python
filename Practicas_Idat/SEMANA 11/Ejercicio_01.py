#Realizar un programa que inicialice una lista con 10 números enteros aleatorios
#(del 1 al 20) y posteriormente muestre en pantalla todos los elementos de la lista
#y luego solo los números pares.

from random import randint # Ingresar los aleatoreos
lista=[] #Declarar lista vacia

for i in range(10): #Generar 10 reiteraciones
    numero=randint(1,20)#Se genera el número aleatorio
    lista.append(numero) #Para insertar al final "append"

for i in range(len(lista)):
    print("lista [{}]:{}".format(i,lista[i]))

#for elemento in lista:
# print(elemento)

for elemento in lista:
    if elemento%2==0:
        print(elemento)