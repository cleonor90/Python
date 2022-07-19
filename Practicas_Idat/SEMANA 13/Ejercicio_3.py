def esPerfecto (numero):
    suma=0
    for i in range(1,numero//2+1):
        if numero%i==0
        suma+=i
    return suma==numero

def listaPerfectos(N):
    lista=[]
    for i in range(1,N+1):
        if esPerfecto(i):
            lista.append(i)
    return lista

numero= int(input("Ingrese "))
