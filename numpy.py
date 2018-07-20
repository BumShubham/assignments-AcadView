import numpy as np
from random import *

#q1
arr = np.random.random((10,1))
print("The mean is:",np.average(arr))

#q2
arr1 = np.random.random((20,1))
print("The variance is:",np.var(arr1))
print("The standard deviation is:",np.std(arr1))

#q3
a = np.random.random((10,20))
b = np.random.random((20,25))
c=np.dot(a,b)
print(c)
print(np.shape(c))
print(np.sum(c))

#q4
arr3 = np.random.random((10,1))
print(arr3)
func = 1/(1+np.exp(-arr3))
print(func)