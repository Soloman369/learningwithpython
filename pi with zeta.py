import numpy as np
import matplotlib.pyplot as plt

N = 100
x = np.arange(1, N+1)
sum_inverse = np.cumsum(1/x)
sum_inverse_squares = np.cumsum(1/x**2)
sum_inverse_cubes = np.cumsum(1/x**3)


plt.plot(x, sum_inverse, label=r'$\sum_{i=1}^{N} 1/x_i$')
plt.plot(x, sum_inverse_squares, label=r'$\sum_{i=1}^{N} 1/{x_i}^2$')
plt.plot(x, sum_inverse_cubes, label=r'$\sum_{i=1}^{N} 1/{x_i}^3$')
plt.xlabel('N')
plt.savefig('destination_path.eps', format='eps', dpi=10000)
plt.legend()




import numpy as np
def zeta(s, N=60000):
    x = np.arange(1, N+1)
    sum_inverse_power = np.cumsum(1/x**s) # cumulated sum 
    return sum_inverse_power[-1] # last element is the best approximation
    
    
    
    print('zeta(2) = ',zeta(2))
pi = np.sqrt(6*zeta(2))
print('pi =', pi)
