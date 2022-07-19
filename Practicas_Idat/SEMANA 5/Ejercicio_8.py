#minuto 1:42

#Ingreso de datos

turno= int(input("Ingrese el turno de mañana (1), noche (2)"))
cantidad= int(input("Ingrese la cantidad"))


#Proceso de datos
if turno==1:
    precio=37.5

else:
    precio=45

importedeCompra=precio*cantidad

if cantidad>=15:
    descuento=importedeCompra*8/100

else:
    


#Imprimir
print("Importe de compraa."+str(importedeCompra))
print("El descuento."+str(descuento))
print("importe a pagar."+str(imp))






