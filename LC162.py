# Find peak element

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if (
                (mid == 0 and nums[mid] > nums[mid+1]) or 
                (mid == r and nums[mid] > nums[mid-1]) or
                (nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1])
                ):
                return mid
            if nums[mid+1] > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return
    
sol = Solution()
nums = [1,2,3,1]
print(sol.findPeakElement(nums))