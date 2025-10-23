# Successful pairs of spells and potions

from typing import List
import math

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        output = []
        for spell in spells:
            count = 0
            l = 0
            r = len(potions) - 1
            target = math.ceil(success/spell)
            #Binary search
            mid = l + (r-l+1)//2
            while l <= r:
                
                if potions[mid] >= target:
                    if mid == 0 or potions[mid - 1] < target:
                        break

                    else:
                        r = mid - 1
                else:
                    l = mid + 1
                mid = l + (r-l+1)//2
                
            count = len(potions) - mid
            output.append(count)
        return output
    
spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
sol = Solution()
print(sol.successfulPairs(spells, potions, success))