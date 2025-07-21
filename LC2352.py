# Equal row and column pair
from typing import List

def equalPairs(grid: List[List[int]]) -> int:
    #hashset = set(grid)
    hashmap = {}
    for row in grid:
        row = tuple(row)
        if row in hashmap:
            hashmap[row] += 1
        else:
            hashmap[row] = 1

    count = 0
    n = len(grid)
    for i in range(n):
        col = []
        for j in range(n):
            col.append(grid[j][i])

        if tuple(col) in hashmap:
            count += hashmap[tuple(col)]

    return count

grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
print(equalPairs(grid))