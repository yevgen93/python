def palindrome(num):
    if num < 0:
        return False

    original = num
    reversed = 0

    # Reverse the original number
    while num > 0:
        reversed = reversed * 10 + num % 10
        num //= 10
    
    return original == reversed



print(palindrome(1221))
print(palindrome(123))
print(palindrome(123321))
