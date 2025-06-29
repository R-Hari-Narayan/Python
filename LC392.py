# Is subsesequence

def isSubsequence(s: str, t: str) -> bool:
    if s == "":
        return True
    if t == "":
        return False
    L = len(s)
    l = 0
    for c in t:
        if c == s[l]:
            l+= 1
        if l == L:
            return True
    return False

s= "abc"
t= "ahbgdc"
print(isSubsequence(s, t))