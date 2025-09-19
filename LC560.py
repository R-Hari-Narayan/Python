# Subarray sum equals K

from typing import List

def subarraySum(nums: List[int], k: int) -> int:
    prefix_sum = []
    sum = 0
    for n in nums:
        sum += n
        prefix_sum.append(sum)

    print(prefix_sum)
    
    prefix_set = set(prefix_sum)
    print(prefix_set)
    count = 0
    for sum in prefix_sum:
        if sum == k or sum-k in prefix_set:
            
            count += 1
    return count

nums = [1]
print(subarraySum(nums, 0))