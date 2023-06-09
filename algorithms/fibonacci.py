# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0
# F(1) = 1
# F(2) = 1
# F(3) = 2
# F(4) = 3
# F(5) = 5
# F(6) = 8
# F(7) = 13
# F(8) = 21
# F(9) = 34
# F(N) = F(N - 1) + F(N - 2), for N > 1.
# Given N, calculate F(N).

# Input: 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# Recursively
def fib_recursive(n):
    if n < 2:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

# Iteratively
def fib_iterative(n):
    a,b = 0,1
    for i in range(n):
        a,b = b, a+b
    return a
 
print(fib_recursive(9))
print(fib_iterative(9))
