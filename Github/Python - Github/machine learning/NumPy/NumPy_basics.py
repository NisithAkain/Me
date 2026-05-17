import numpy as np 
import sys

a = np.array([1,2,3], dtype="int16") # declaring data type 
print(a)

b=np.array([[1,2,3],[5,6,7]])
print(b)

print(a.ndim) # dimention of array
print(b.shape) # size of array

print(a.itemsize)

print(a.size)