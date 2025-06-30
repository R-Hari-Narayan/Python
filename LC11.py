#Container with most water
from typing import List

def maxArea(height: List[int]) -> int:
    maximumArea = 0 
    l= 0
    r = len(height)-1
    while l<r:
        area = min(height[l], height[r]) * (r-l)
        if area > maximumArea:
            maximumArea = area
        if height[l]> height[r]:
            r-=1
        else:
            l+=1
    return maximumArea

height = [1,8,6,2,5,4,8,3,7]
print((maxArea(height)))