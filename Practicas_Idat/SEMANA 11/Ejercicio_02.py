#Realizar un programa que inicialice una lista con 10 valores (del 1 al 10) y
#posteriormente muestre en pantalla cada elemento de la lista junto con su
#cuadrado y su cubo

lista=[]

for i in range (1,11): #Muestra en el rango del 1 al 10
    lista.append(i)  #Agregue el valor en i 

for elemento in lista: #Por cada elemento en la lista
    print("{}\t{}\t{}".format (elemento,(elemento**2),(elemento**3)))
    

