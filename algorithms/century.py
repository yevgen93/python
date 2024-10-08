# Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

# Example

# For year = 1905, the output should be
# solution(year) = 20;
# For year = 1700, the output should be
# solution(year) = 17.

def solution(year):
    # If the year is exactly divisible by 100, it is at the end of a century
    if year % 100 == 0:
        return year // 100
    # Otherwise, compute the century by integer division and adding 1
    return (year // 100) + 1
