#Two sum
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    hashMap = dict()
    for i,n in enumerate(nums):
        hashMap[n] = i

    for i,n in enumerate(nums):
        requiredNumber = target-n
        if requiredNumber in hashMap and hashMap[requiredNumber]!= i:
            return [i, hashMap[requiredNumber]]

print(twoSum([3,2,4], 6))