# Removing stars from a string

def removeStars(s: str) -> str:
    stack = []
    for ch in s:
        if ch != "*":
            stack.append(ch)
        else:
            stack.pop()
    return "".join(stack)

s = "leet**cod*e"
print(removeStars(s))