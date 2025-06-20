#Reverse vowels of a string

def reverseVowels(s: str) -> str:
    s= list(s)
    l = 0
    r = len(s)-1
    vowels = set("aeiouAEIOU")
    while l<r:
        #Find left vowel
        while l<r and s[l] not in vowels:
            print("l:",l)
            l+=1
        print("l:",l)
        #Find right vowel
        while l<r and s[r] not in vowels:
            print("r:",r)
            r-=1
        print("r:",r)
        #Swap vowels
        s[l], s[r] = s[r], s[l]
        l+=1
        r-=1

    return "".join(s)

s = "leetcode"
print(reverseVowels(s))