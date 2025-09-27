# Number of recent calls

class RecentCounter:

    def __init__(self):
        self.q = []
        

    def ping(self, t: int) -> int:
        while self.q and t - self.q[0] > 3000:
            self.q.pop(0)
        self.q.append(t)
        return len(self.q)
        


obj = RecentCounter()
print(obj.ping(642))
print(obj.ping(1849))
print(obj.ping(4921))
print(obj.ping(5936))
print(obj.ping(5957))