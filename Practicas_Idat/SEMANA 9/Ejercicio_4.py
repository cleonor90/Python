#Diseñe un programa que imprima y sume a siguiente serie
#100,97,94,91,...,16,13,10.

suma=0
for i in range(100,7,-3):
    print(i,end=" ")
    suma+=i

print("\nSuma: "+str(suma))