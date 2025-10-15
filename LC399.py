# Evaluate Division

from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #Create a weighted directed graph
        graph = defaultdict(list)
        visited = defaultdict(bool)

        for i, e in enumerate(equations):
            graph[e[0]].append((e[1], values[i]))
            graph[e[1]].append((e[0], 1/values[i]))

        print(graph)

        def dfs(root, targetNode):
            visited[root] = True
            if graph[root] == []:
                return -1
            if root == targetNode:
                return 1
            for child in graph[root]:
                if not visited[child[0]]:
                    if child[0] == targetNode:
                        return child[1]
                    n = dfs(child[0], targetNode)
                    if n != -1:
                        return child[1] * n
            return -1
        
        output = []
        for q in queries:
            visited = defaultdict(bool)
            output.append(dfs(q[0], q[1]))

        return output
    
sol = Solution()
equations = [["a","b"]]
values = [0.5]
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
print(sol.calcEquation(equations, values, queries))