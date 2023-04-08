# write a python program using numpy module to create an arrary and check the type of array,dimension , shape

import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9])
print("Array element :",a)
print("Type: ",a.dtype)
print("Dimension :",a.ndim)
print("Shape",a.shape)
print()
b= np.array([[1.2,2.3],[4.5,6.8],[7.8,9.6]])
print("Array Element :",b)
print("Type: ",b.dtype)
print("Dimension :",b.ndim)
print("shape :",b.shape)
