# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
# https://neetcode.io/problems/anagram-groups

# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]


def anagram_groups(strs):
  # Create a dictionary to hold the anagram groups
  anagram_map = {}

  # Loop thru each string in the input list
  for word in strs:
    
    # Sort the word and use it as a key
    sorted_word = ''.join(sorted(word))

    # If the key is not in the dictionary, add it with an empty list
    if sorted_word not in anagram_map:
      anagram_map[sorted_word] = []

    # Append the original word to the list for this sorted key
    anagram_map[sorted_word].append(word)

  # Return the grouped anagrams as a list of lists
  return list(anagram_map.values())
