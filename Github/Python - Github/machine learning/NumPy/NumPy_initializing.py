import numpy as np 


a = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
print(f'normal 1d vector {a}')


a = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]).reshape(4,4)
print(f'a reshaped matrix,{a.ndim}d, \n {a}')