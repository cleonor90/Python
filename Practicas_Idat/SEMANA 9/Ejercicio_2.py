#Diseñe un programa que imprima y sume la siguiente serie:
#100, 99, 98, …, 1

suma=0 #Se debe agregar como segundo paso para sumar
for i in range(100,0,-1): #Debe ser 0 porque si pongo 1 será si pongo 1 sería 2 #El menos 1 hace decreciente
    print(i,end=" ")
    suma+=i #Se debe agregar para sumar

print("\nSuma: "+ str(suma))


