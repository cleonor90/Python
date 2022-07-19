from random import randint

c1h=0
c2h=0
c3h=0
c4h=0
c5h=0

for i in range (75):
    h=randint(1,5)
    if h==1:
        c1h+=1
    elif h==2:
        c2h+=1
    elif h==3:
        c3h+=1
    elif h==4:
        c4h+=1
    else:
        c5h+=1

print ("\nCantidad de personas con 1 hijo: " + str (c1h))
print ("\nCantidad de personas con 2 hijo: " + str (c2h))
print ("\nCantidad de personas con 3 hijo: " + str (c3h))
print ("\nCantidad de personas con 4 hijo: " + str (c4h))
print ("\nCantidad de personas con 5 hijo: " + str (c5h))