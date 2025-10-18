# Rotting Oranges

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #Find all rotten oranges
        q= deque()
        m = len(grid)
        n = len(grid[0])
        freshCount = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i, j])
                elif grid[i][j] == 1:
                    freshCount += 1
        if len(q) == 0 and freshCount == 0:
            return 0
        #BFS
        minute = -1
        def rotOrange(x, y):
            if x in range(0, m) and y in range(0, n) and grid[x][y]== 1:
                grid[x][y] = 2
                q.append([x,y])
                return 1
            return 0
        while q:
            minute += 1
            for _ in range(len(q)):
                rottenOrange = q.popleft()
                x = rottenOrange[0]
                y = rottenOrange[1]
                
                freshCount -= rotOrange(x-1, y) #top
                freshCount -= rotOrange(x+1, y) #bottom
                freshCount -= rotOrange(x, y-1) #left
                freshCount -= rotOrange(x, y+1) #right

        return minute if freshCount == 0 else -1

sol = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(sol.orangesRotting(grid))