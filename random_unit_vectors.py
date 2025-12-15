## Write a function:
## `random_unit_vectors(num_vectors, dim)` that:
## a)creates a matrix M of shape (num_vectors, dim)using;
## M = np.random.randn(num_vectors, dim)
## b)normalizes each row so it has Euclidean norm 1,
## c)returns the resulting matrix as a NumPy array.
#%%
import numpy as np

def random_unit_vectors(num_vectors, dim):
    
    M = np.random.randn(num_vectors, dim)
    
    norms = np.linalg.norm(M, axis=1)
    
    M_normalized = M / norms[:, np.newaxis]
    
    return M_normalized

print(random_unit_vectors(5, 3))
    
    

    
    





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

