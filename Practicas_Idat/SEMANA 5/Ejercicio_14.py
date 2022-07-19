#ingreso de datos
from xml.dom.xmlbuilder import DOMImplementationLS


numuero_oculto=int(input("Ingrese numero oculto: "))
importe_compra=float(input("ingrese el importe de la compra: "))

#Validación

if numuero_oculto%2==0 and numuero_oculto>=100:
    descuento=importe_compra*15/100

else:
    descuento=importe_compra*5/100

importe_pagar=importe_compra-descuento


print("importe descuento : " + str (descuento))
print("Importe a pagar: " + str(importe_pagar))
   