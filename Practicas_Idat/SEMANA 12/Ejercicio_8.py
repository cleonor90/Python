#Escriba una función que reciba como parámetro un año y devuelve True o
#False según el año sea bisiesto o no.
#Un año es bisiesto si es múltiplo de 4 pero no múltiplo de 100, aunque los
#múltiplos de 400 sí lo son. Estos son algunos ejemplos de posibles respuestas:
#2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto

def esbisiesto(año):
    if año%400==0:  #si el año es multiplo de 400 y da residuo 0 
        return True
    elif año%100==0:
        return False
    elif año%4==0:
        return True
    else:
        return False  #Aqui tomamos todos los numeros que no son multiplos de 4 ni de 100 ni 400

print (2012, esbisiesto(2012)) #Evaluando los años


#Estos son algunos ejemplos de posibles respuestas:
#2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto



        
