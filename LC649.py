# Dota2 Senate
from collections import deque

def predictPartyVictory(senate: str) -> str:
    rq, dq = deque(), deque()
    n = len(senate)
    for index, ch in enumerate(senate):
        if ch == "R":
            rq.append(index)
        else:
            dq.append(index)
    while rq and dq:
        r = rq.popleft()
        d = dq.popleft()
        if r< d:
            rq.append(r+n)
        else:
            dq.append(d+n)
    
    if rq:
        return "Radiant"
    else:
        return "Dire"

print(predictPartyVictory("RDD"))