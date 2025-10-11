# Number of provinces

from typing import List
from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = []
        for node, _ in enumerate(isConnected):
            visited = False
            for province in provinces:
                if node in province:
                    visited = True
                    break
            if visited:
                continue
            #Since not in any province, create a new province
            province = set()
            #bfs
            q = deque([node])
            while q:
                n = q.popleft()
                province.add(n)
                for index, connected in enumerate(isConnected[n]):
                    if connected and index not in province:
                        q.append(index)
            provinces.append(province)
        return len(provinces)
    
sol = Solution()
isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
print(sol.findCircleNum(isConnected))