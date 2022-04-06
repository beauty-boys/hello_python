import numpy as np
y = np.zeros(188,int)
l = []
a = 90/(94*94)
b = -180/94
c = 120
for i in range(188):
    y[i] = a*i*i+b*i+c
    l.append(y[i])
print(y)
print(l)