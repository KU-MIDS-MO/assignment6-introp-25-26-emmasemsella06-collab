## Write a function:
## `estimate_pi(num_samples)` that:
## returns an estimate of π using num_samples random points generated with np.random.rand().

import numpy as np

def estimate_pi(num_samples):
    inside_circle = 0
    
    for i in range(num_samples):
        x = np.random.rand()
        y = np.random.rand()
        
        if x**2 + y**2 <= 1:
            inside_circle += 1
            
    pi_estimate = 4 * inside_circle / num_samples
    return pi_estimate

print(estimate_pi(1000))
print(estimate_pi(100000))
