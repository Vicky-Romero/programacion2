import matplotlib.pyplot as plt
import numpy as np
import random
from PIL import Image, ImageOps

iml=Image.open("gojo.jpg")
imlgr=ImageOps.grayscale(iml)
arim=np.array(imlgr)

fila=450
columna=800
aux=0

for i in range(fila):
    for j in range(int(columna/2)):
        aux=arim[i][j]
        inop=columna-1-j
        arim[i][j]=arim[i][inop]
        arim[i][inop]=aux
       
    

plt.imshow(arim, cmap="gray")
plt.show()