#Maximum average subarray
from typing import List

def findMaxAverage(nums: List[int], k: int) -> float:
    #Calculate avg of first k
    maxAvg = 0.0
    sum = 0
    for i in range(k):
        sum+= nums[i]
    maxAvg = sum/k
    #Move the window to find other avgs
    l= 0
    r= k
    while r< len(nums):
        sum += nums[r]
        sum -= nums[l]
        newAvg = sum/k
        if newAvg > maxAvg:
            maxAvg = newAvg
        l+= 1
        r+= 1
    return maxAvg

nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums, k))