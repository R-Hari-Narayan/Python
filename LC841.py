# Keys and Rooms

from typing import List
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visitedRooms = set()
        keys= deque([0])
        while keys:
            room = keys.popleft()
            visitedRooms.add(room)
            for key in rooms[room]:
                if key not in visitedRooms:
                    keys.append(key)
        return len(visitedRooms) == len(rooms)
    
sol = Solution()
rooms = [[1,3],[3,0,1],[2],[0]]
print(sol.canVisitAllRooms(rooms))