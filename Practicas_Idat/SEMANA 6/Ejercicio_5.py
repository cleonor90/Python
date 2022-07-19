#ingreso de datos
codigo=int(input("Ingrese el codigo del producto: "))
unidades=int(input("Ingrese las unidades obtenidas: "))


#Proceso de datos
if codigo==101 or codigo==102 or codigo==103:
    unidades=int(input("Ingrese la cantidad de unidades: "))
    if unidades>0:
        if codigo==101:
         precio_u=17.5
    elif codigo==102:
         precio_u=25
    elif codigo==103:
         precio_u=15.5

importeCompra=precio_u*unidades

if unidades>=1 and unidades<=10:
    descuento=importeCompra*5/100
elif unidades>=1 and unidades<=20:
    descuento=importeCompra*7.5/100
elif unidades>20:
    descuento=importeCompra*10/100

importepagar=importeCompra-descuento

#Imprimir
print("importe de compra: "+ str(importeCompra))
print("Descuento: "+ str(descuento))
print("Importe a pagar: "+str(importepagar))



