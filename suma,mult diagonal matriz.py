suma=0
mult=1
cmult=1
csuma=0
matriz=[[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16]]
for i in range(4):
    print()
    for j in range(4):
        print(matriz[i][j],end=" ")
        if(i==j):
            suma=suma+matriz[i][j]
        if(i==j):
            mult=mult*matriz[i][j]
        if(j==i):
            csuma=csuma+matriz[i][j]
        if(j==3-1):
            cmult=cmult*matriz[i][j]
print()
print("La suma de la diagonal es ",suma)
print("La multiplicación de la diagonal es ",mult)
print("La suma de la contradiagonal es ",csuma)
print("La multiplicación de a contradiagonal es ",cmult)