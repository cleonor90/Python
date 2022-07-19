#Diseñe un programa que imprima y sume 20 terminos de la siguiente serie:
#7,9,13,15,20,22,28,30,37
#+2 +4 +2 +5 +2 +6 +2 +7

termino=7  #Mi primer termino o numero es 7
razonimpar=2 #En los impares aument2 2
razonpar=4

for i in range(1,21):
    print(termino,end=" ")
    if i%2==0:
        termino+=razonpar
        razonpar+=1

    else:
        termino+=razonimpar
