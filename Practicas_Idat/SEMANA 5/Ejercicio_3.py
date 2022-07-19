#Para ayudar a los alumnos en la evaluación del curso, el profesor ha prometido
#incrementar en dos puntos la nota del examen, si es que esta es no menor que
#11. Diseñe un programa que determine la nota de un alumno. Considere que la
#nota máxima es 20.

#Ingreso de datos
nota=float(input("Ingrese su nota: "))

#Proceso de datos

if nota<0 or nota>20:   #validación
    mensaje = -1
if nota>=11:
    nota+=2
if nota>20:
    nota=20

#Mostrar resultado

if nota==-1:
    print("Nota no valida")

if nota!=-1:
    print("Su nota será: " + str(nota))

