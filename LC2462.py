# Total cost to hire k workers

from typing import List
import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        l = candidates
        r = len(costs)- candidates
        if l> r:
            r = l
        lHeap = costs[0:l]
        rHeap = costs[r:]
        heapq.heapify(lHeap)
        heapq.heapify(rHeap)
        totalCost = 0
        for _ in range(k):
            print("lHeap: ", lHeap)
            print("rHeap: ", rHeap)
            if not rHeap or (lHeap and lHeap[0] <= rHeap[0]):
                totalCost += heapq.heappop(lHeap)
                if l < r:
                    heapq.heappush(lHeap, costs[l])
                    l+= 1
            else:
                totalCost += heapq.heappop(rHeap)
                if r > l:
                    r-= 1
                    heapq.heappush(rHeap, costs[r])
            

        return totalCost
    
sol = Solution()
costs = [57,33,26,76,14,67,24,90,72,37,30]
k = 11
candidates = 2
print(sol.totalCost(costs, k, candidates))