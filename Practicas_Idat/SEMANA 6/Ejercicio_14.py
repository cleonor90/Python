#Ingreso de datos
categoria=input("Ingrese la categoria(A-B-C-D): ")
promedio=float(input("Ingrese el promedio: "))

#Proceso 
if categoria=="A":
    pension=3000

elif categoria=="B":
    pension=2500

elif categoria=="C":
    pension=2000

else:
    pension=1500

if promedio<14:
    descuento=0
elif promedio<14 and promedio<16:
    descuento=pension*10/100

elif promedio<18:
    descuento=pension*12/100
else:
    descuento=pension*15/100

nuevaPensión=pension-descuento

#Mostrar resultados
print("Pensión actual: "+ str(pension))
print("Descuento: "+str(descuento))
print("Nueva pensiión: "+str(nuevaPensión))