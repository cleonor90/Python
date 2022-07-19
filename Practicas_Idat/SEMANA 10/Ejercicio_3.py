from random import randint

sumanotas=0
mayor=1
menor=21

for i in range(1,46):
    nota=randint(0,20)
    print("nota {}: {}".format(i,nota))

    if nota>mayor:
        mayor=nota
    if nota<menor:
        menor=nota
    
    sumanotas+=nota

promedio=round(sumanotas/45,2)

print("Nota mayor: " +str(mayor))
print("Nota menor: " +str(menor))
print("Nota promedio: " +str(promedio))

