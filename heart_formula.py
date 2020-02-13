import matplotlib.pyplot as plt
import numpy as np

def heart_1(x):
    return sqrt(1-(abs(x)-1)**2)
def heart_2(x):
    return -3*sqrt(1-(abs(x)/2)**0.5)

x = np.linspace(-2,2,1000)
y1 = np.vectorize(heart_1)
y2 = np.vectorize(heart_2)

plt.plot(x,y1(x))
plt.plot(x,y2(x))
plt.show()
