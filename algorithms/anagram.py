# Given an input of two strings, write a method to determine if the two strings are anagrams 
# (composed of the same set of letters) of each other. Letter uppercase/lowercase state is ignored.
# Sample inputs:
# isAnagramMatch("melon", "lemon") => true
# isAnagramMatch("ocean", "canoe") => true
# isAnagramMatch("battle", "tablet") => true
# isAnagramMatch("reserve", "reverse") => true
# isAnagramMatch("bob", "rob") => false
# isAnagramMatch("tape", "tap") => false

# Without using return sorted(str1) == sorted(str2)

def isAnagramMatch(str1, str2):
    # Edge case if the strings are diff lengths
    if len(str1) != len(str2):
        return False

    # Build a hash map for each string with key/value pairs consisting of the letter and it's frequency in the string
    map1, map2 = {}, {}

    # Hashmap for first string
    for letter in range(0,len(str1)):
        l = str1[letter]
        if l in map1.keys():
            map1[l] += 1
        else:
            map1[l] = 1
    
    # Hashmap for second string
    for letter in range(0,len(str2)):
        l = str2[letter]
        if l in map2.keys():
            map2[l] += 1
        else:
            map2[l] = 1
    
    # The two strings are anagrams if the corresponding maps are identical
    return map1 == map2
    


print(isAnagramMatch("melon","lemon"))
print(isAnagramMatch("ocean","canoe"))
print(isAnagramMatch("battle","tablet"))
print(isAnagramMatch("reserve","reverse"))
print(isAnagramMatch("bob","rob"))
print(isAnagramMatch("tape","tap"))
