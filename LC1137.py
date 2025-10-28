# N-th Tribonacci number

class Solution:
    tribonacciArray = [0,1,1] + [None] * 35
    def tribonacci(self, n: int) -> int:
        if self.tribonacciArray[n]!= None:
            return self.tribonacciArray[n]
        self.tribonacciArray[n] = self.tribonacci(n -1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        return self.tribonacciArray[n]
    
sol = Solution()
print(sol.tribonacci(37))