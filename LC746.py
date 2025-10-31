# Min cost climbing stairs

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] += cost[i - 1] if cost[i - 1] < cost[i - 2] else cost[i -2]
        return cost[-1] if cost[-1] < cost[-2] else cost[-2]
    
sol = Solution()
cost = [10,15,20]
print(sol.minCostClimbingStairs(cost))