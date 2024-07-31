import datetime
fecha=datetime.date.today()
hora=datetime.datetime.now()
print(fecha)
print(hora)
nacimiento=0
mes=0
dia=0
edad=0
nacimiento=int(input("Ingrese su año.."))
mes=int(input("su mes.."))
dia=int(input("y su dia de nacimiento.."))
edad=fecha-nacimiento-mes-dia
print("Su edad es ",edad)