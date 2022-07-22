def NumeroPerfecto(num):
    suma=1
    for i in range(2,num):
        if (num % i ==0):
            suma+=i
    if num==suma:
        return True
    else:
        return False

def suma(a,b):
    resultado=a+b
    return resultado 

def multiplicacion(c,d):
    resultado=c*d
    return resultado
