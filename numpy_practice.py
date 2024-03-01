import numpy as np
import time
import sys

size= 1000000

l1= list(range(size))
l2= list(range(size))

start= time.time()
result= [(x+y) for x,y in zip(l1,l2)]
print("Python list took: ", (time.time()- start)* 1000)

a1= np.arange(size)
a2= np.arange(size)

start= time.time()
result= a1+a2
print("Numpy array took: ", (time.time()- start)*1000)

print("Size of python array: ", sys.getsizeof(1)* size)
print("Size of numpy array : ", a1.size* a1.itemsize)