# Decode string

def decodeString(s: str) -> str:
    stack = []
    output = ""
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    isOpen = 0
    for ch in s:
        if (ch not in numbers) and (len(stack) == 0):
            output+= ch
        else:
            if ch != "]":
                if ch == "[":
                    isOpen += 1
                stack.append(ch)
            else:
                isOpen -= 1
                tmp = []
                while stack[-1] != "[":
                    tmp.insert(0, stack.pop())
                tmp = "".join(tmp)
                stack.pop()
                number = []
                while len(stack)!= 0 and stack[-1] in numbers:
                    number.insert(0, stack.pop())
                number = int("".join(number))
                if isOpen:
                    stack.append(number * tmp)
                else:
                    output += number * tmp
        print(stack)
    return output

s= "abc3[cd]xyz"
print(decodeString(s))