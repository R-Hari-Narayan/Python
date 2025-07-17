# Longest subarray of 1's after deleting one 
from typing import List

def longestSubarray(nums: List[int]) -> int:
    l=0
    max_w = 0
    no_zeros = 0
    for r in range(len(nums)):
        if nums[r] == 0:
            no_zeros += 1
        
        if no_zeros > 1 :
            #Invalid window
            while nums[l] != 0 and l< r:
                l+=1
            l+=1
            no_zeros -= 1

        max_w = max(max_w, r-l)

    return max_w

nums = [1,1,1]
print(longestSubarray(nums))