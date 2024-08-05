# Given an input of two strings, write a method to determine if the two strings are anagrams 
# (composed of the same set of letters) of each other. Letter uppercase/lowercase state is ignored.
# Without using return sorted(str1) == sorted(str2)

def isAnagramMatch(str1, str2):
    # Edge Case / strings are different lengths
    if len(str1) != len(str2):
        return False
    
    # Build hashmap per word of letter : count_of_letter
    map1, map2 = {}, {}

    for letter in str1:
        if letter not in map1:
            map1[letter] = 1
        else:
            map1[letter] += 1

    for letter in str2:
        if letter not in map2:
            map2[letter] = 1
        else:
            map2[letter] += 1

    # The two strings are anagrams if the corresponding maps are identical
    return map1 == map2

print(isAnagramMatch("melon", "lemon")) # True
print(isAnagramMatch("ocean", "canoe")) # True
print(isAnagramMatch("battle", "tablet")) # True
print(isAnagramMatch("reserve", "reverse")) # True
print(isAnagramMatch("bob", "rob")) # False
print(isAnagramMatch("tape", "tap")) # False
