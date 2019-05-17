# Fib value at index n
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(6))

# Fib sequence
# https://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence 
def fibb():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b

for index, fibonacci_number in zip(range(10), fibb()):
     print('{i}: {f}'.format(i=index, f=fibonacci_number))
