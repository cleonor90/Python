from random import randint
sumaEdades=0
contadorEdades=0
contadorMayor=0
contadorMenor=0

while True:
    edad = randint(14,70)
    contadorEdades+=1
    sumaEdades+=edad
    print("La persona N° {} tiene {} años de edad".format(contadorEdades,edad))

    if edad >=18:
        contadorMayor+=1
    else:
        contadorMenor+=1

    if edad > 45 and edad < 50 :
        break
promedio = round(sumaEdades/contadorEdades,2)

print("\nEl promedio de edades es: " + str(promedio))
print("La cantidad de mayores de edad: " + str(contadorMayor))
print("La cantidad de menores de edad: " + str(contadorMenor))