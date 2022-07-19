import random
lista = []

for i in range(3):
    lista.append([])
    # print(lista)
    for z in range(5):
        lista[i].append(random.randint(10, 99))

for j in range(3):
    print(lista[j])

fila = len(lista)
culmnas = len(lista[i])
lista2=[]

for n in range(culmnas):
    suma = sum([fila[n] for fila in lista])
    lista2.append(suma)

print(lista2)