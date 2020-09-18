# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.
# Given N, calculate F(N).

# Input: 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# Recursively
class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N
        else:
            return self.fib(N - 1) + self.fib(N - 2)
            
# Iteratively
class Solution:
    def fib(self, N: int) -> int:
        a,b = 0,1
        for _ in range(N):
            a,b = b, a+b
        return a
