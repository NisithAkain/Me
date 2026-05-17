import numpy as np 

a = np.array([[1,2,3,4,5,6,7,8,9,10], [11,12,13,1,41,16,19,201,1,3]])
print(a)


print(a[1,5]) # specfic item 
print(a[0,:]) # everything in first row
print(a[:, 0])


print(a)
a[0,1] = 201
print(a)