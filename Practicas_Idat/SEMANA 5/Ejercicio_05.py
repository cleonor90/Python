#Una tienda vende tres tipos de productos cuyos códigos son 101, 102, 103 y 104
#a los precios unitarios dados en la siguiente tabla:

#Ingreso de datos
codigo= int(input("Código de producto (101-102-103-104): ") )
unidades=int(input("Unidades: "))

#Proceso
if codigo ==101:
    precioUnitario = 17.5

if codigo == 102 or codigo ==104:
    precioUnitario =25

if codigo ==103:
    precioUnitario = 15.5

importeCompra= precioUnitario * unidades

if unidades>=1 and unidades>=10:
    descuento=importeCompra * 5/100

if unidades>=11 and unidades>=20:
    descuento=importeCompra * 7.5/100

if unidades>=20:
    descuento=importeCompra * 10/100
