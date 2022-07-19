#Escriba una función que reciba como parámetro un año y devuelve True o
#False según el año sea bisiesto o no.
#Un año es bisiesto si es múltiplo de 4 pero no múltiplo de 100, aunque los
#múltiplos de 400 sí lo son. Estos son algunos ejemplos de posibles respuestas:
#2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto

def bisiesto(a):
    if (a%4==0 and a%100!=0) or (a%400==0 and a%100!=0):
        return "True"
    else: return "False"
año=int(input("El año es: "))
print(bisiesto(año))

