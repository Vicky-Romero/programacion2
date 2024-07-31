import random
numrand=0
intentos=0
numingre=0

numrand=random.randint(1,20)
while(intentos<6):
    numingre=int(input("Ingrese un número entre 1 y 20:.."))
    intentos=intentos+1
    if numingre==numrand:
        print("Felicidades encontro el número secreto")
        break
    else:
        if numingre>numrand:
                print("El número ingresado es mayor al número secreto")
        else:
            print("El número ingresado es menor a número secreto")

if intentos==6:
    print("¡Ups! Se le acabaron los intentos, usted pierde.El número secreto era ",numrand)
else:
    print("..")

    

    