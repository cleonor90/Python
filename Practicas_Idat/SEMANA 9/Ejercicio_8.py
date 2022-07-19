#Diseñe un programa que imprima y sume 25 terminos de la siguiente serie:
#2,7,4,9,11,16,13

posicion_impares=2
posiciones_pares=7
suma=0 #Se agrega para la suma***

for i in range(1,25):
    if i%2!=0:   #Si la posición es diferente de 0 es decir impar
        print(posicion_impares, end=" ")
        suma+=posicion_impares  #Se agrega para la suma ***
        posicion_impares=2 #Ya que la siguiente posición sera 4 - 8 - 16

    else:
        print(posiciones_pares, end=" ")
        suma+=posiciones_pares #Se agrega para la suma ****
        posiciones_pares+=2

#Si quiero sumar se agrega***  Suma+=posicionimpar

print("\nSuma: "+str (suma))



