#Diseñe un programa que imrpima y sume 10 terminos de la siguiente serie  #9,16,25,36,49,64
#3*3=9 // 4*4=16// 5*5=25//6*6=36//7*7=49//8*8=64

termino=3
suma=0
for i in range(10):
    cuadrado=termino**2  #Elevado al cuadrado
    print(cuadrado,end=" ")
    termino+=1
    suma+=cuadrado

print("\nSuma: "+str(suma))


