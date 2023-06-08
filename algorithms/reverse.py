# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# You may assume all the characters consist of printable ascii characters.
 
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

def reverse(s):
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

print(reverse(["h","e","l","l","o"]))

# Allocate extra space
# def reverse(str):
#     final = []
#     n = (len(str)-1)
#     while n > -1:
#         final.append(str[n])
#         n -= 1
#     return ''.join(final)

# print(reverse('cat'))
