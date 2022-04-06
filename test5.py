from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# fl ='D:\\image\\2022.3.9\\01\\'
# name ='.jpeg'
# file=fl+'116'+name
fl = 'D:\\image\\2022.3.9\\04\\'
number = 115
name = '.jpeg'
file = fl + str(number) + name
a = np.asarray(Image.open(file).convert('L')).astype('int')
b = np.zeros(256,int)
for i in range(len(a)):
    for j in range(len(a[i])):
        b[a[i][j]] +=1
plt.hist(b,bins=100,range=[0,100],rwidth=100)
plt.show()