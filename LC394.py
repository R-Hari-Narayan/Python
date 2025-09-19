# Decode string

def decodeString(s: str) -> str:
    stack = []
    output = ""
    for ch in s:
        if ch != "]":
            stack.append(ch)
        else:
            tmp = []
            while stack[-1] != "[":
                tmp.insert(0, stack.pop())
            tmp = "".join(tmp)
            stack.pop()
            output += int(stack.pop()) * tmp
        print(stack)
                
    return output

s= "3[a2[c]]"
print(decodeString(s))