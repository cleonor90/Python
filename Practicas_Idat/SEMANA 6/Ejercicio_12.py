#Ingreso de datos
horas_trabajadas=int(input("Ingrese las horas trabajadas: "))
categoria=input("Ingrese la categoria: ")


#Proceso de datos

if categoria=="A":
    tarifa=21
    
elif categoria=="B":
    tarifa=19.5

elif categoria=="C":
    tarifa=17

else: 
    tarifa=15.5

sueldobruto=tarifa*horas_trabajadas

if sueldobruto>25000:
    descuento=sueldobruto*20/100
else:
    descuento=sueldobruto*25/100

sueldoneto=sueldobruto-descuento

#Muestra resultados