#Escriba una función que reciba como parámetros dos años y devuelva una
#lista con los años bisiestos comprendidos en el rango (incluidos los dos años).

def esbisiesto(año):
    if año%400==0:  #si el año es multiplo de 400 y da residuo 0 
        return True
    elif año%100==0:
        return False
    elif año%4==0:
        return True
    else:
        return False

def listabiciestos(inicio,fin):
    lista=[]
    for año  in range(inicio,fin+1):
        if esbisiesto(año):
            lista.append(año)
    return lista

año1=int(input("Año inicio: "))
año2=int(input("Año fin: "))

lista=listabiciestos(año1,año2)

print ("Años bisiestos entre {} y {}: {}".format(año1,año2,lista))

