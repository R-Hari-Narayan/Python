# Search insert position

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        mid = l + (r - l)//2
        while l <= r:
            mid = l + (r-l)//2
            print("mid: ", mid, "l: ", l, "r: ", r)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return mid if nums[mid] > target else mid + 1
    
sol = Solution()
nums = [1,3,5,6]
target = 4
print(sol.searchInsert(nums, target))