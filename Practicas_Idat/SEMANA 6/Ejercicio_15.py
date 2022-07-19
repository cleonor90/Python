tipo=int(input("Tipo de chocolates(1-2-3-4): "))


if tipo>=1 and tipo<4:
    cantidad=int(input("Cantidad de chocolates: "))
    if cantidad>1:
        #Proceso
        if tipo==1:
            precio=8.5
        elif tipo==2:
            precio=10
        elif tipo==3:
            precio=7
        else:
            precio=12.5

        importe_Compra=precio*cantidad

        if cantidad<5:
            descuenti=importe_Compra*4/100
        elif cantidad<10:
            descuenti=importe_Compra*6.5/100
        elif cantidad<15:
            descuenti=importe_Compra*9/100
        else:
            descuenti=importe_Compra*11/100

        importepagar=importe_Compra-descuenti

        if importepagar>=250:
            caramelos=cantidad*3
        else:caramelos=cantidad*2

        #Mostrar resultados
        print("importe de compra"+ str(importe_Compra))
        print("importe de compra"+ str(descuenti))
        print("importe de compra"+ str(importepagar))
        print("importe de compra"+ str(caramelos))

    else:
        cantidad("Cantidad no valida")
else:
    print("Tipo no valido")

        



