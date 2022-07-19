superior=1
inferior=1
suma=0

for i in range(1,16):
    print(superior, "/", inferior )
    suma+=superior/inferior
    superior+=5
    inferior+=4

print("\nLa suma es: " + str (round(suma,2)))