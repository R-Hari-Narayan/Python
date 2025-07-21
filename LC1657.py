# Determine if two strings are close


def closeStrings(word1: str, word2: str) -> bool:
    hashmap1 = Counter(word1)
    hashmap2 = Counter(word2)

    if hashmap1 == hashmap2:
        return True
    
    hashset1 = set(hashmap1.keys())
    hashset2 = set(hashmap2.keys())

    hashmap3 = Counter(hashmap1.values())
    hashmap4 = Counter(hashmap2.values())
    
    if hashset1 == hashset2 and hashmap3 == hashmap4:
        return True
    return False


def Counter(word: str):
    hashmap = {}
    for letter in word:
        if letter in hashmap:
            hashmap[letter]+= 1
        else:
            hashmap[letter] = 1

    return hashmap
word1 = "cabbba"
word2 = "abbccc"
print(closeStrings(word1, word2))