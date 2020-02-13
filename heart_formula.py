import matplotlib.pyplot as plt
import numpy as np

def heart_1(x):
    return np.sqrt(1-(np.abs(x)-1)**2)
def heart_2(x):
    return -3*np.sqrt(1-(np.abs(x)/2)**0.5)
    
x = np.linspace(-2,2,1000)
y1 = heart_1(x)
y2 = heart_2(x)
    
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()
