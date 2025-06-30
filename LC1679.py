#Max number of K sum pairs
from typing import List

def maxOperations(nums: List[int], k: int) -> int:
    hashmap = {}
    maxOp = 0
    for n in nums:
        if n in hashmap:
            hashmap[n]+= 1
        else:
            hashmap[n] = 1
    print("hashmap: ", hashmap)

    for n in nums:
        target = k-n
        if target in hashmap and hashmap[target] > 0:
            hashmap[target]-= 1
            hashmap[n]-= 1
            if hashmap[n]< 0:
                hashmap[n]+= 1
                hashmap[target]+= 1
            else:
                maxOp += 1
            

    print("hashmap: ", hashmap)
    return maxOp

nums = [1,2,3,4]
k = 5
print(maxOperations(nums, k))