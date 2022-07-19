#Diseñe un programa que simule el lanzamiento de 3 dados hasta que salga el mismo numero en los 3 dados
#Imprima los puntajes obtenidos en cada dado y la cantidad de lanzamientos efectuados

from random import randint
from random import I  #Cuando me hablan de aleatorio lo primero es importar ramdom /N aleatorios

i=1  ## Este es el contador

while True:
    dado1=randint(1,6)
    dado2=randint(1,6)
    dado3=randint(1,6)
    print("Lanzamiento #{}: {},{},{}". format(i,dado1,dado2,dado3))
    if dado1==dado2 and dado2==dado3:
        break  #Sin este brak caemos en un bucle infinito
    i+=1 #Si este acumulador no suma no tendriamos el valor de las veces que lanzamos y solo seria 1 ,1,1,1,1
 


