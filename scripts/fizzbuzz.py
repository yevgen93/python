def fizz():
    for x in range(1, 100):
        if (x % 3 == 0) and (x % 7 == 0):
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 7 == 0:
            print("Buzz")
        else: 
            print x
fizz()

# Write a program that runs through an ordered list of numbers (1-100) and 
# for each multiple of 3 prints Fizz, 
# for each multiple of 7 prints Buzz. 
# If it's multiple of both 3 & 7, print FizzBuzz. 
# Otherwise print the number itself
# Sample output:
# 1
# 2
# Fizz
# 4
# 5
# Fizz
# Buzz
# 8
# Fizz
# 10
# 11
# Fizz
# 13
# Buzz
# Fizz
# 16
# 17
# Fizz
# 19
# 20
# FizzBuzz
# 22
