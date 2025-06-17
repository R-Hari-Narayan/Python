# LeetCode problem number 169
from typing import List


def majorityElement(nums: List[int]) -> int:
    visited: List[int] = []
    count = 0
    Len = len(nums)
    for x in nums:
        if x not in visited:
            visited.append(x)
            for num in nums:
                if num == x: 
                    count += 1
            if count > (Len/2):
                return x
    return -1



nums: List[int] = [2,2,1,3,1,1,4,1,1,5,1,1,6]
ans: int = majorityElement(nums= nums)

print(ans)