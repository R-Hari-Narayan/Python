# Reorder routes to make all paths lead to the city zero

from typing import List
from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        directed = set()

        # Build graph and track directed edges
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            directed.add((a, b))  # original direction

        visited = [False] * n

        def dfs(node: int) -> int:
            visited[node] = True
            count = 0
            for nei in graph[node]:
                if not visited[nei]:
                    # if edge is directed away from 0, we need to reorder
                    if (node, nei) in directed:
                        count += 1
                    count += dfs(nei)
            return count

        return dfs(0)
    
sol = Solution()
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
n = len(connections)  + 1
print(sol.minReorder(n, connections))