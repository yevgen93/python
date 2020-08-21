# A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# Also, a self-dividing number is not allowed to contain the digit zero.
# Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
# Input: 
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

def isSelfDivNum(number):
    num = str(number)
    for digit in num:
        if (digit == "0") or (number % int(digit) != 0):
            return False
    return True

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        final = []
        for number in range(left, right+1):
            if isSelfDivNum(number):
                final.append(number)
        return final
