#Crear una función que, a partir de dos números, devuelva su punto
#intermedio. El número intermedio de dos números corresponde a la suma de
#los dos números dividida entre 2.

def intermedio(b,a):
    return (b+a)/2

a=float(input("Ingrese primer número: "))
b=float(input("Ingrese 2do número: "))


print("El valor intermedio es", intermedio(b,a))