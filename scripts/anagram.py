# Given an input of two strings, write a method to determine if the two strings are anagrams 
# (composed of the same set of letters) of each other. Letter uppercase/lowercase state is ignored.
# Sample inputs:
# isAnagramMatch("melon", "lemon") => true
# isAnagramMatch("ocean", "canoe") => true
# isAnagramMatch("battle", "tablet") => true
# isAnagramMatch("reserve", "reverse") => true
# isAnagramMatch("bob", "rob") => false
# isAnagramMatch("tape", "tap") => false

def isAnagramMatch(str1, str2):
    if len(str1) != len(str2):
        return False
    letterFrequencyMap = {}
    for letter in range(0, len(str1)):
        if str1[letter] in letterFrequencyMap.keys():
            letterFrequencyMap[str1[letter]] += 1
        else:
            letterFrequencyMap[str1[letter]] = 1
    for letter in range(0, len(str2)):
        if str2[letter] in letterFrequencyMap.keys() and letterFrequencyMap[str2[letter]] > 0:
            letterFrequencyMap[str2[letter]] -= 1
        else:
            return False
    return True


print(isAnagramMatch("melon","lemon"))
print(isAnagramMatch("ocean","canoe"))
print(isAnagramMatch("battle","tablet"))
print(isAnagramMatch("reserve","reverse"))
print(isAnagramMatch("bob","rob"))
print(isAnagramMatch("tape","tap"))