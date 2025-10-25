# Letter combinations of a phone number

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2": ("a", "b", "c"),
                   "3": ("d", "e", "f"),
                   "4": ("g", "h", "i"),
                   "5": ("j", "k", "l"),
                   "6": ("m", "n", "o"),
                   "7": ("p", "q", "r", "s"),
                   "8": ("t", "u", "v"),
                   "9": ("w", "x", "y", "z")
                   }
        def dfs(index = 0, s= ""):
            if index == len(digits):
                return [s]
            output = []
            for child in mapping[digits[index]]:
                output += dfs(index+1, s+child)
            return output
        return dfs()
    
sol = Solution()
digits = "23"
print(sol.letterCombinations(digits))