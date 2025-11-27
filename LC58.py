# Length of Last Word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
    
sol = Solution()
s = "luffy is still joyboy"
print(sol.lengthOfLastWord(s))