# Find the difference of two arrays
from typing import List

def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    nums1_set = set(nums1)
    nums2_set = set(nums2)
    output = [[], []]
    for n in nums1_set:
        if n not in nums2_set:
            output[0].append(n)
    for n in nums2_set:
        if n not in nums1_set:
            output[1].append(n)
    return output

nums1 = [1,2,3]
nums2 = [2,4,6]
print(findDifference(nums1, nums2))