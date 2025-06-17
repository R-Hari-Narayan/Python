#DSA 1: Selection sort

from typing import List


def selection_sort(nums: List[int]) -> List[int]:
    min_index = 0
    length = len(nums)
    for index in range(length):

        #default min value to be at start
        min_index = index

        #search for min value position
        for i in range(index, length):
            if nums[i] < nums[min_index]:
                min_index = i
        
        #Swap value at index with min value index
        nums[index], nums[min_index] = nums[min_index], nums[index]
    
    return nums


#main
nums = [10, 9, 8, 7, -6, 5, 4, 3, 2, 1, 32]
sorted_nums = selection_sort(nums)
print(sorted_nums)