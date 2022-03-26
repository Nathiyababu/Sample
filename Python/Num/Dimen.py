import numpy as np
#0th dimension array or scalars
x=np.array(20)
#1-d array or uni-dimension array
y=np.array([1,2,3,4,5,6,7])
#2-d
z=np.array([[1,2,3],[4,5,6]])
#3-d
a=np.array([[[1,2,3],[4,5,6],[1,2,3],[4,5,6]]])
#Higher Dimension
b=np.array([1,2,3,4,5],ndmin = 5)
print(x.ndim)
print(y.ndim)
print(z.ndim)
print(a.ndim)
print("Higher Dimension:", b)
