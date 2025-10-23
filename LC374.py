# Guess number higher or lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

def guess(num: int) -> int:
    global pick
    if num == pick:
        return 0
    elif num > pick:
        return -1
    else:
        return 1

class Solution:
    def guessNumber(self, n: int) -> int:
        def binSearch(l, r):
            if l > r:
                return -1
            mid = l + int((r-l)/2)
            res = guess(mid)
            if res == 0:
                return mid
            elif res == -1:
                return binSearch(l, mid-1)
            else:
                return binSearch(mid+1, r)

        return binSearch(1, n)
    
sol = Solution()
n = 10
pick = 6
print(sol.guessNumber(n))