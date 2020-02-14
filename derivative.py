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

def expenential(x):
    return np.exp(x)
y_expenential = expenential(x)
plt.plot(x,y_expenential)
plt.show()

def reverse(x):
    return -1/(x**2)
y_reverse = reverse(x)
plt.plot(x,y_reverse)
plt.show()

def logarithme(x):
    return 1/x
y_logarithme = logarithme(x)
plt.plot(x,y_logarithme)
plt.show()
