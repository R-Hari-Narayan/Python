# Range sum query- immutable
from typing import List

class NumArray:
    prefix_sum = [0]

    def __init__(self, nums: List[int]):
        for n in nums:
            self.prefix_sum.append(n + self.prefix_sum[-1])
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right+1] - self.prefix_sum[left]

nums = [-1]
obj = NumArray(nums)
param_1 = obj.sumRange(0,0)
print(param_1)