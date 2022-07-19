#Entrada de datos
precio_xciento=float(input("ingrese el precio por ciento: "))
cantidad_xciento=int(input("ingrese la cantidad por ciento: "))

#proceso

if  cantidad_xciento>=5:
    if cantidad_xciento>=5:
        descuento=precio_xciento*cantidad_xciento*10/100

    else:
        descuento=(precio_xciento*5*100/100)+(precio_xciento*(cantidad_xciento-5)*15/100)

importebruto= precio_xciento*cantidad_xciento
importeapagar=importebruto-descuento

print("El importe bruto es: " +str(importebruto))
print("El importe a pagar es: "+str(importeapagar))
      
    
