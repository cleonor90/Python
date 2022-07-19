from random import randint
cantAprobados=0
cantDesaprobados=0
sumaNotas=0


for i in range(40):
    nota=randint(0,20)
    sumaNotas+=nota
    print(nota, end=" ")
    if nota>=13:
        cantAprobados+=1
    else:
        cantDesaprobados+=1

promedio=round(sumaNotas/40,2)

print("\nNota promedio: " + str (promedio))
print("Cantidad de desaprobados: " + str (cantDesaprobados))
print("Cantidad de aprobados: " + str (cantAprobados))