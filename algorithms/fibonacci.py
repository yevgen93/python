# Function for nth Fibonacci number
# 0 1 1 2 3 5 8 13 21 34 55 89 144

def fib(n):
    if n < 0:
        print("Incorrect input")

    # First Fibonacci number is 0
    elif (n == 1):
        return 0

    # Second Fibonacci number is 1
    elif (n == 2):
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(9))

# Fib sequence

def fibSequence(n):
	a,b = 0,1

	for x in range(n):
		yield a
		a,b = b, a+b

for num in fibSequence(10):
	print(num)
