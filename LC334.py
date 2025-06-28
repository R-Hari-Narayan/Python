# Increasing triplet subsequence
from typing import List
import sys

def increasingTriplet(nums: List[int]) -> bool:
    i = sys.maxsize
    print(i)
    j= sys.maxsize
    for n in nums:
        if n<= i:
            i = n
        elif n<= j:
            j = n
        else:
            return True
    return False

nums = [2,1,5,0,4,6]
print(increasingTriplet(nums))