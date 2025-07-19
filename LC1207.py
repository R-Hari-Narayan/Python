# Unique number of occurences
from typing import List
from collections import Counter

def uniqueOccurrences(arr: List[int]) -> bool:
    d=Counter(arr)
    print(d)
    hashmap = {}
    for n in arr:
        if n in hashmap:
            hashmap[n]+= 1
        else:
            hashmap[n] = 1

    hashset = set()
    for value in hashmap.values():
        if value in hashset:
            return False
        else:
            hashset.add(value)

    return True

arr = [1,2,2,1,1,3]
print(uniqueOccurrences(arr))