import math
import matplotlib.pyplot as plt
import numpy as np

def heart_1(x):
    return sqrt(1-(abs(x)-1)**2)
def heart_2(x):
    return -3*sqrt(1-(abs(x)/2)**0.5)
    

x = np.linspace(-2,2,1000)
y1 = []
y2 = []
for i in x :
    y1.append(heart_1(i))
    y2.append(heart_2(i))
    
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()
