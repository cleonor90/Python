from random import randint
i=1
while True:
    edad=randint(25,80)
    estadoCivil=randint(1,4)
    if estadoCivil==1:
        desEstadoCivil="Soltero"
    elif estadoCivil==2:
        desEstadoCivil="Casado"
    elif estadoCivil==3:
        desEstadoCivil="viudo"
    else:
        desEstadoCivil="Divorsiado"
    print("Persona N°{}: Edad={} Estado Civil={}". format(i,edad,desEstadoCivil))
    
    if edad==80:
        break
    i+=1 
print("Ultimo estado civil generado: "+str(desEstadoCivil))
    
