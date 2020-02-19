import math
def is_prime(x):
    max_to_verify = int(math.sqrt(x))
    # loop from 2 --> sqrt(x), because 1 divides all numbers
    for i in range(2, max_to_verify):
        if x % i == 0: # if i divides x, x not prime
            return False
    return True
   
 
print(is_prime(5))
### Output = True
