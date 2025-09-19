# Asteroid collision
from typing import List

def asteroidCollision(asteroids: List[int]) -> List[int]:
    stack = []
    for asteroid in asteroids:
        if asteroid < 0:
            while len(stack)> 0 and stack[-1] < -asteroid:
                stack.pop()
            if len(stack) == 0:
                stack.append(asteroid)
            elif stack[-1] == -asteroid:
                stack.pop()
        else:
            stack.append(asteroid)

    return stack

asteroids = [-2,-1,1,2]
print(asteroidCollision(asteroids))