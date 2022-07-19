#Crear una función que reciba dos números positivos y devuelva el número
#menor. Si ambos son iguales debe devolver el mensaje: “Los números son
#iguales”

def calcularmenor(b,a):
    if a<b:
        return a
    elif b<a:
        retur: b
    else:
        return "Los numeros son iguales"


numero1=int(input ("1er numero: "))
if numero1>0:
    numero2=int(input("2do numero: "))
    if numero2>0:
        menor=calcularmenor(numero1,numero2)
        print("EL menor es :",menor)
    else:
        print("El 2do numero debe ser positivo")
else:
    print("El primero número debe ser positivo")

