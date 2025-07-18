# Find pivot index
from typing import List

def pivotIndex(nums: List[int]) -> int:
    prefix = ['0'] * len(nums)
    sum = 0
    for i, n in enumerate(nums):
        sum += n
        prefix[i] = sum

    for i, n in enumerate(prefix):
        lhs = prefix[i-1] if i>0 else 0
        rhs = sum - n
        if lhs == rhs:
            return i

    return -1

nums = [1,7,3,6,5,6]
print(pivotIndex(nums))