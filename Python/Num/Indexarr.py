import numpy as np
#1st dimension indexing
y=np.array(["Hello",2,"Nathiya"])
print(y[0] + y[2])
#2nd dimentsion indexing
x=np.array([[1,2,3],[4,5,6]])
#print(x[0])
#print(x[1])
print(x[0,2])
print(x[1,1])
#3rd dimension
y=np.array([[[1,2,3],[4,5,6],[1,2,3],[4,5,9]]])
print(y[0,3,2])
print(y[0,1,2])
print(y[0,-1,-1])


