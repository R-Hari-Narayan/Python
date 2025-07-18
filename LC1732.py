# Find the highest altitude
from typing import List

def largestAltitude(gain: List[int]) -> int:
    max_alt = 0
    curr_alt = 0
    for n in gain:
        curr_alt += n
        max_alt = max(max_alt, curr_alt)
    return max_alt

gain = [-5,1,5,0,-7]
print(largestAltitude(gain))