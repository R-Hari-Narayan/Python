import numpy as np
import time
import sys

size= 1000

l= list(range(5))
print(l)

arr= np.arange(5)
print(arr)

print(sys.getsizeof(1)* 5)
print(arr.itemsize* arr.size)