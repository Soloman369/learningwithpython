import numpy as np

class Dice():
    def __init__(self):
        self.choices = [1,2,3,4,5,6]
    
    def sample(self):
        return np.random.choice(self.choices)
        
        
for i in range(10):
    throw_1 = Dice()
    print(throw_1.sample())
