class Solution(object):
    def is_prime(self,num):
        # Edge cases
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        
        # Start the loop from 5 and check for factors up to square root of num.
        # Increment by 6 each step to skip even numbers and multiples of 3.
        # Any factor of the form 6k +- 1 is sufficient to find all prime factors.
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
        
    def countPrimes(self, n):
        count = 0
        for i in range(2,n):
            # Use self to refer to the method in the same class
            if self.is_prime(i):
                count += 1
        return count
        
