import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(1,10,100)

def derive(x):
    return 1/(2*np.sqrt(x))
y_derive = derive(x)
plt.plot(x,y_derive)
plt.show()

def square(x):
    return 2*x
y_square = square(x)
plt.plot(x,y_square)
plt.show()

def cube(x):
    return 3*(x**2)
y_cube = cube(x)
plt.plot(x,y_cube)
plt.show()

def exponential(x):
    return np.exp(x)
y_exponential = exponential(x)
plt.plot(x,y_exponential)
plt.show()

def reverse(x):
    return -1/(x**2)
y_reverse = reverse(x)
plt.plot(x,y_reverse)
plt.show()

def logarithm(x):
    return 1/x
y_logarithm = logarithm(x)
plt.plot(x,y_logarithm)
plt.show()
