texto=input("Ingrese el texto que quiere cifrar:..").upper()
desp=int(input("ingrese el desplazamiento:.."))
def cifrar(texto,desp):
    resultado="" 
    for i in texto:
        lenum=ord(i)+desp
        if (lenum>ord("Z")):
            lenum=lenum-26
                     
        if (lenum<ord("A")):
            lenum=lenum+26
            
 
        numle=chr(lenum)
            
        resultado=resultado+numle
        
    return resultado
print(cifrar(texto,desp))