# Task 1
# First 20 fibonacci numbers

# Define function
def fib(a):
    # Stops parameter from being less than 1
    if a <= 1:
        return a
    else:
        # Fibonacci calculation
        return fib(a - 1) + fib(a - 2)


# Range to allow loop 20 times
for i in range(20):
    print(str(fib(i)), end=" ")
