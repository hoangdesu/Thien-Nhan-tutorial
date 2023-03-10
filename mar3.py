# anagram

def checkAnagram(s1: str, s2: str) -> bool:
    # if s1 and s2 are anagram:
    #     return True
    # else:
    #     return False
    
    s1 = s1.strip().replace(' ', '').lower()
    s2 = s2.strip().replace(' ', '').lower()
    
    if len(s1) != len(s2):
        return False
    
    s1CharMap = {}
    for c in s1.lower():
        if c in s1CharMap:
            s1CharMap[c] += 1
        else:
            s1CharMap[c] = 1
            
    print(s1CharMap)
    
    s2CharMap = {}
    for c in s2.lower():
        if c in s2CharMap:
            s2CharMap[c] += 1
        else:
            s2CharMap[c] = 1
            
    print(s2CharMap)
    
    return s1CharMap == s2CharMap
    
print('1', checkAnagram("Tom Marvolo Riddle", "I am Lord Voldemort")) # -> True
print('2', checkAnagram("abc", "cbz")) # -> False
print('3', checkAnagram('care', 'race'))

assert(checkAnagram('', 'a'))

# l1 = [1,2,3]
# l2 = [1,3,2]

# print(l1 == l2)

# o1 = { 'a': 1, 'b': 2 }
# o2 = { 'b': 2, 'a': 1 }

# print(o1 == o2)