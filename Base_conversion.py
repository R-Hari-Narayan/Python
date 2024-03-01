def Base_convert(word):
    value= 0
    pow = 0
    for i in range(-1, -len(word)-1, -1):
        value+= (ord(word[i])-96) * (26 ** pow)
        pow += 1
    return value

word= input("Enter a word : ")
print(Base_convert(word))