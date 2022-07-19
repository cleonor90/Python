#Diseñe un programa que genere números aleatorios en el intervalo de 1 a 1000
#hasta obtener un número con cuatro divisores. El programa mostrará un listado
#como el siguiente:
#N121  cantidad de divisores 3
#N881  cantidad de divisores 2
#N60 cantidad de divisores 12
#N978  cantidad de divisores 8
#N964  cantidad de divisores 6
#N22  cantidad de divisores 4

from random import randint


print("numero\tcantidad de divisores")

while True:
    numero=randint(1,1000)
    cantidad=0
    for i in range (1,numero+1):
        if numero%i==0:
            cantidad+=1

    print(str(numero)+"\t"+str(cantidad))
    if cantidad==4:
        break
    
        
        


    