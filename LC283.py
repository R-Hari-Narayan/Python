# Move zeroes
from typing import List

def moveZeroes(nums: List[int]) -> None:
    L = len(nums)
    if L ==1:
        return
    i = 0
    while nums[i] != 0 and i< L:
        i+=1
    j = i+1
    while j< L:
        if nums[i] == 0 and nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i+= 1 
            j+= 1
        else:
            j+= 1
    return


nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)


# def moveZeroes(nums: List[int]) -> None:
#     count = 0
#     for n in nums:
#         if n == 0:
#             count += 1
#     for i in range(count):
#         nums.remove(0)
#     nums += count* [0]
#     return