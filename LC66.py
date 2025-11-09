# Plus one

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        number = 0
        digits.reverse()
        for index, n in enumerate(digits):
            number += n * pow(10, index)
        number += 1
        number = str(number)
        return [int(s) for s in number]
        
    
sol = Solution()
digits = [9]
print(sol.plusOne(digits))