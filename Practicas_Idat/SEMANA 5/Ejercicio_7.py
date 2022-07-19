#Ingreso de datos
donacion= float(input("Donación $."))

#Proceso de datos

if donacion<=10000:
    centroSalud=donacion*30/100 
    comedorNiños=donacion*50/100
    bolsa=donacion-(centroSalud-comedorNiños)

else:
    donacion>=10000
    centroSalud=donacion*25/100
    comedorNiños=donacion*60/100
    bolsa=donacion-(centroSalud-comedorNiños)

#Imprimir
print("Centro de salud: $."+str(centroSalud))

print("Comedor de niños: $."+str(comedorNiños))

print("Bolsa de valores: $."+str(bolsa))