# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ, product = 0,1
        while n > 0:
            digit = n%10
            summ += digit
            product *= digit
            n //= 10
        return product - summ
