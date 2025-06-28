#String Compression
from typing import List

def compress(chars: List[str]) -> int:
    currentChar = chars[0]
    count = 0
    s = []
    for char in chars:
        if char == currentChar:
            count += 1
        else: 
            s.append(currentChar)
            if count> 1:
                s.append(str(count))
            currentChar = char
            count = 1
    s.append(currentChar)
    if count> 1:
        s.append(str(count))
    s= "".join(s)
    for i, char in enumerate(s):
        chars[i]= s[i]
    return len(s)

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(compress(chars))