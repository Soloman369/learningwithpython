#### Iterative method ####

def factorial(x):
    a = 1
    for i in range(x+1):
        if i == 0: continue
        print(i)
        a *= i
    return a
    
  
#### Recursive method ####

def factorial(x):
    if x == 1:
        return 1
    else: return x * factor(x-1)
    
