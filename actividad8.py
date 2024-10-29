import matplotlib.pyplot as plt
import numpy as np
import random
from PIL import Image, ImageOps

iml=Image.open("gojo.jpg")
arim=np.array(iml)


plt.imshow(arim, cmap='gray')
plt.show()

fila=450
columna=800
grises=np.zeros((450,800))

for i in range(fila):
    for j in range(int(columna)):
        grises[i][j]=arim[i][j][0]*0.2989+arim[i][j][1]*0.5870+arim[i][j][2]*0.1140

plt.imshow(grises, cmap='gray')
plt.show()