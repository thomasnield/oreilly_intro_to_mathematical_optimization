import numpy as np


value = 6.0
fifth_root_candidate = value / 2.0

for i in range(100000):
    adjust = np.random.standard_t(3, 1)[0]
    new_candidate =  fifth_root_candidate + adjust 
    
    if  (value - fifth_root_candidate ** 5) ** 2 > (value - new_candidate ** 5) ** 2:
        fifth_root_candidate = new_candidate
        

print(fifth_root_candidate)
