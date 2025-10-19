# Kth largest element in an array

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        k = len(nums)- k
        for _ in range(k):
            heapq.heappop(nums)
        return heapq.heappop(nums)
    
sol = Solution()
nums = [3,2,1,5,6,4]
k = 2
print(sol.findKthLargest(nums, k))

# Sotution 1
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         nums.sort(reverse=True)
#         return nums[k-1]