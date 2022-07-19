#IMPRIMA Y SUME 12 TERMINOS SERIE/6/8/12/20/36
#6,8,12,20,36
#+2 +4 +8 +16

termino=6
razon=2
suma=0 #Si quiero la suma se agrega 1

for i in range (12):
    print(termino,end=" ")
    suma+=termino #Se agrega para la suma 2
    termino+=razon
    razon*=2

print("\nSuma:" + str )