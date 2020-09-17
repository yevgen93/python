# Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # create a dictionary and add all key/occurence pairs
        # compare the length of the dict values against the length of the set of dict values
        # set returns unique values
        d = {}
        for num in arr:
            if num not in d.keys():
                d[num] = 1
            d[num] += 1
        return len(d.values()) == len(set(d.values()))
