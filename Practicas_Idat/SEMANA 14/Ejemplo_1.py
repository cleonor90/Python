def sumarTuplas(t1,t2,t3):

    lista=[]

    suma=0

    for i in range(len(t1)):

        suma=t1[i]+t2[i]+t3[i]

        lista.append(suma)

    return tuple(lista)



x = (1, 2, 3, 4)

y = (3, 5, 2, 1)

z = (2, 2, 3, 1)



tuplaSuma = sumarTuplas(x,y,z)

print(tuplaSuma)