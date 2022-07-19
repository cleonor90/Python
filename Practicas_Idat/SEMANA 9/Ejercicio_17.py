contador=0

for i in range (100,901):
    if i%3==0:
        print(i, end=" ")
        contador+=1

print("\n La cantidad de multiplos de 3 fueron: "+str(contador))