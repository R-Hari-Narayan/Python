#Max consecutive ones III
from typing import List

def longestOnes(nums: List[int], k: int) -> int:
    max_w = 0
    no_zeroes = 0
    l= 0
    r= 0
    while r< len(nums):
        if (nums[r] == 1) or (nums[r]== 0 and no_zeroes < k):
            #valid
            if r-l+1 > max_w:
                max_w = r-l+1
            if nums[r] == 0:
                no_zeroes += 1
        else :
            #invalid
            no_zeroes += 1
            while no_zeroes > k and l<= r:
                #print("l", l)
                if nums[l]== 0:
                    no_zeroes -= 1
                l+= 1
        r+=1
        print("r", r)
        print("l", l)
        print("max_w", max_w)
        print("no_zeroes", no_zeroes)
    return max_w

nums = [0,0,1,1,1,0,0]
k = 0
print(longestOnes(nums, k))