from typing import List

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    count = 0
    flowerbed = [0] + flowerbed + [0]
    for i in range(1, len(flowerbed)-1):
        if not (flowerbed[i] or flowerbed[i-1] or flowerbed[i+1]) :
            flowerbed[i] = 1
            count += 1

    print(flowerbed)
    print(count)

    return n <= count

flowerbed = [1,0,0,0,1]
n = 2

print(canPlaceFlowers(flowerbed, n))