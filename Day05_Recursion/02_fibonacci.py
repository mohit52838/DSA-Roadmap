# Fibonacci using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Alternative: Using loop
'''
def fibonacci_iter(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a+b
'''

# User Input
n = int(input("\nEnter number of terms: "))
print("Fibonacci Sequence:")
for i in range(n):
    print(fibonacci(i), end = " ")