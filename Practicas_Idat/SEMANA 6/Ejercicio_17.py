#Ingreso de datos
cuadernos_cantidad=int(input("Ingrese el número de cuadernos adquiridos: "))

#Ingreso de datos
if cuadernos_cantidad<12:
    lapicero=0
    novo=0
    cross=0

elif cuadernos_cantidad<24:
    lucas=cuadernos_cantidad//4
    novo=0
    cross=0

elif cuadernos_cantidad<36:
    lucas=0
    novo=0
    cross=(cuadernos_cantidad//4)*2

else:
    lucas=1
    novo=(cuadernos_cantidad//4)*2
    cross=1

#Mostrar resultado
print("lucas: " +str(lucas))
print("Novo: " +str(novo))
print("cross: " +str(cross))
