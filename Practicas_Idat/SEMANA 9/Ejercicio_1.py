#Diseñe un programa que imprima y sume la siguiente serie:
# 0,1,2,3, … ,50

suma=0
for i in range(51): #Ya que si solo dejo 50 llega a 49
    print(i,end=" ")
    suma+=i

print("\nSuma: "+str (suma))  #\n salto de linea para que no salga todo junto con lo de arriba

#Aqui no hay opcion que entre en un bucle infinito , ya que la variable control se aumenta de 1 en 1
#Con la funcion range



#Con while 
#i=0
#while i<=50:
#    print(i,end=" ")
#   i+=1 // aqui debo incrementar