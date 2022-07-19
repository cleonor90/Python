numero=23456
#Quiero obtener el 2 ejemplo
print(numero//1000) #Dara resultado 2

#Quiero obtener numero 3
print(numero//100)

a= numero//1000
b=numero//100%10
c=numero//10%10
d=numero%10

suma=a + b + c + d
producto= a* b * c * d

print("Suma: "+ str(suma))
print("Producto: "+ str(producto))
