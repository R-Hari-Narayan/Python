# Nearest exit from entrance in maze

from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        
        #bfs
        q= deque([entrance])
        maze[entrance[0]][entrance[1]] = "v"
        layer = -1
        while q:
            layer += 1
            for _ in range(len(q)):
                node = q.popleft()
                x = node[0]
                y = node[1]
                #maze[x][y] = "v" #Mark as visited
                #Check if node is exit
                if (x == 0 or y == 0 or x== m-1 or y == n-1) and layer > 0:
                    return layer
                #top
                if x-1 >= 0 and maze[x-1][y] == ".":
                    q.append([x-1, y])
                    maze[x-1][y] = "v"
                #bottom
                if x+1 < m and maze[x+1][y] == ".":
                    q.append([x+1, y])
                    maze[x+1][y] = "v"
                #left
                if y-1 >= 0 and maze[x][y-1] == ".":
                    q.append([x, y-1])
                    maze[x][y-1] = "v"
                #right
                if y+1 < n and maze[x][y+1] == ".":
                    q.append([x, y+1])
                    maze[x][y+1] = "v"

        return -1
    
sol = Solution()
maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
entrance = [1,2]
print(sol.nearestExit(maze, entrance))