#Diseñe un programa que genere aleatoriamente las edades de 45 personas con valores del intervalo 18 a 70
#Determine: 
#Edad promedio /// La cantidad de personas menores o iguales a 30 años /// La cantidad de personas mayores a 30

from random import randint   #Cuando me hablan de aleatorio lo primero es importar ramdom /N aleatorios

sumaedades=0  #Como quiere saber promedio debo sumar todas las edades
canmenoroiguala30=0
cantidadmayor30=0

for i in range (45):
    edad=randint(18,70)      #Aqui genero la edad en el rango
    if edad>30:
        cantidadmayor30+=1
    else:
        canmenoroiguala30+=1
    sumaedades+=edad             #Acumular la edad y sumo la edad que genere aleatoriamente

promedio=round(sumaedades/45,2)     #Necesitamos sacar el promedio la suma entre las 45 / redondeo 2 dec

print("Cantidad de mayores a 30: "+ str (cantidadmayor30))
print("Cantidad de menores o iguales a 30: " + str (canmenoroiguala30))
print("El promedio es : "+ str(promedio))



