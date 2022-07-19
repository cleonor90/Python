#Escriba una función que tome una lista de números enteros y devuelva dos
#listas ordenadas. La primera con los números pares y la segunda con los
#números impares.

def separarparesdeimpares(lista):
    listadepares=[]
    listadeimpares=[]
    for elemento in lista:
        if elemento%2==0:
            listadepares.append(elemento)
        else:
            listadeimpares.append(elemento)
    
    return listadepares,listadeimpares

lista= [6,5,2,1,7]
pares,impares=separarparesdeimpares(lista)

print(pares)
print(impares)

