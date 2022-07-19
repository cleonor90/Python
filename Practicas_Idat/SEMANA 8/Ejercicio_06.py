n=int(input("Ingrese el numero natural "))

i=1
contador=0 
while i<=n: #Recorremos desde 1 while hata el mismo numero
    if n%i==0: #Si el residuo entre el valor de i , si esa división tiene como residuo 0. Se establece que es divisible
        print(i, end="")
        contador+=1

    i+=1

print("\nNumero de divisores "+ str(contador))

