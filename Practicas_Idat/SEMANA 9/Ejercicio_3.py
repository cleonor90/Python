#Diseñe un programa que imrpima y sume la siguiente serie
#10,12,14,...,98,100

suma=0
for i in range(10,101,2):
    print(i,end=" ")
    suma+=i
print("\nSuma: "+str(suma))