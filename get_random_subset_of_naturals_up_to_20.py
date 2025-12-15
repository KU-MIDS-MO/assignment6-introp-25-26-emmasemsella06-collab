## Write a function:
## `get_random_subset_of_naturals_up_to_20()` that:
## outputs a random subset of the set of integers between $1$ and $20$ in the format of a `numpy` array.
## The draw of the subset should be uniform, i.e., any subset should in principle have the same chance to be outputted
## by your function. This problem will be graded manually.
## For $2$ out of the $5$ points allotted to this problem, you can write your function however you wish.
## To get $5$ points, your function is allowed to make a single call to the `numpy.random.randint()` method
## but it cannot make use of any other random methods.

import numpy as np

def get_random_subset_of_naturals_up_to_20():
    
    random_number = np.random.randint(0, 2**20)
    
    subset = []
    
    for i in range(20):
        if (random_number >> i) & 1:
            subset.append(i + 1)
            
    return np.array(subset)

print(get_random_subset_of_naturals_up_to_20())



