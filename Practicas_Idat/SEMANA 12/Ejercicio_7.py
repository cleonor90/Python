#Crear una función llamada rectángulo que reciba como parámetros el alto, el
#ancho y un carácter, luego dibuje el rectángulo con el carácter ingresado.
#Ejemplo: Si los parámetros ingresados son: 3,10,* el rectángulo dibujado
#será: **********
#######**********
#######**********


def rectangulo(alto, ancho, caracter):
    for i in range(alto):
        print(caracter*ancho)  #Operador de replica **** repite tantas veces como indique el ancho

alto=int(input("ingrese el alto: "))
ancho=int(input("ingrese el ancho: "))
caracter=input("ingrese el caracter: ")

rectangulo(alto,ancho,caracter)



