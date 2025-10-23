# Koko eating banana

from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        r = max(piles)
        l = math.ceil(sum(piles)/h)
        output = r
        #Binary search
        while l<= r:
            mid = l + (r-l)//2
            count = 0
            for pile in piles:
                count += math.ceil(pile/mid)
            # print("l: ", l, ", mid: ", mid, ", r: ", r, ", count: ", count, sep= "")
            if count <= h:
                output = mid
                r = mid-1
            else:
                l = mid+1
                
        return output
    
sol = Solution()
piles = [3,6,7,11]
h = 8
print(sol.minEatingSpeed(piles, h))