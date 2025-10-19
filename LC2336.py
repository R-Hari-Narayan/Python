# Smallest number in infinite set

import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.q = [1]
        self.heap = []

    def popSmallest(self) -> int:
        if self.heap:
            return heapq.heappop(self.heap)
        output = heapq.heappop(self.q)
        heapq.heappush(self.q, output+1)
        return output

    def addBack(self, num: int) -> None:
        if num >= self.q[0] or num in self.heap:
            return
        heapq.heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
obj = SmallestInfiniteSet()
print(obj.addBack(2))
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.addBack(1))
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.popSmallest())