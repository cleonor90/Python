#Escriba una función que reciba como parámetro un número “N” y devuelva
#como parámetro el factorial de “N”. Para calcular el factorial, se multiplica el
#número ingresado por los números anteriores hasta llegar a uno. Por
#ejemplo, si introducimos un 5, realizara esta operación 5*4*3*2*1=120.

def factorial(n):

    producto=1
    for i in range(n,0,-1):
        producto*=i
    return producto



numero = int(input("Ingrese un número: "))
print ("El factorial de {} es: {}".format(numero,factorial(numero)))