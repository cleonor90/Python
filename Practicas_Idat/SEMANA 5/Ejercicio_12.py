#ingreso de datos
nota_fundamentosP=int(input("ingrese la nota de fundamentos de programación: "))
desarrollo_p=int(input("Ingrese la nota de desarrollo personal: "))
comunicacion_1=int(input("ingrese la nota de comunicación_1: "))

#Proceso de datos
if nota_fundamentosP>17:
    propina_fp=(nota_fundamentosP)*3
else:
    propina_fp=(nota_fundamentosP)*1

if desarrollo_p>15:
    propina_dp=(desarrollo_p)*2
else:
    propina_dp=(desarrollo_p)*.5

if comunicacion_1>16:
    propinacomunicacion=(comunicacion_1)*1.5
else:
    propinacomunicacion=(comunicacion_1)*.3

if nota_fundamentosP>18:
    regalo="ganaste un reloj"
else:
    regalo="ganaste un lapicero"

propina_total=propina_dp+propina_fp+propinacomunicacion

#imprimir
print("El total de la propina es: " + str(propina_total))
print("El regalo es : " + str(regalo))









