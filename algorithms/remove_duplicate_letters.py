# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
# the smallest in lexicographical order
#  among all possible results.

 

# Example 1:

# Input: s = "bcabc"
# Output: "abc"
# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"

  def removeDuplicateLetters(s):
      # Step 1: Calculate the last occurrence index for each character
      last_occurrence = {char: index for index, char in enumerate(s)}
      
      final = []
      seen = set()
      
      for index, char in enumerate(s):
          # Skip if the character is already in final
          if char in seen:
              continue
          
          # Maintain the smallest lexicographical order
          while final and final[-1] > char and last_occurrence[final[-1]] > index:
              seen.remove(final.pop())
          
          final.append(char)
          seen.add(char)
      
      return ''.join(final)
