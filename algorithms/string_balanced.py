# Balanced strings are those who have equal quantity of 'L' and 'R' characters.
# Given a balanced string s split it in the maximum amount of balanced strings.
# Return the maximum amount of splitted balanced strings.

# Input: s = "RLRRLLRLRL"
# Output: 4

# Input: s = "RLLLLRRRLR"
# Output: 3

def balancedStringSplit(self, s: str) -> int:
    counter, final = 0,0
    for char in s:
        if char == "L":
            counter += 1
        else:
            counter -= 1
        if counter == 0:
            final += 1
    return final
