#Maximum number of vowels in a substring of given lenght

def maxVowels(s: str, k: int) -> int:
    vowels = set("aeiou")
    maxCount = 0
    #Count all vowels in fist k chars
    for i in range(k):
        if s[i] in vowels:
            maxCount += 1
    #Now move the window to count vowels in other substrings
    l = 0
    r = k
    count = maxCount
    while r< len(s):
        if s[r] in vowels:
            count += 1
        if s[l] in vowels:
            count -= 1
        maxCount = max(count, maxCount)
        l+=1
        r+=1
        
    return maxCount

s= "abciiidef"
k= 3
print(maxVowels(s, k))