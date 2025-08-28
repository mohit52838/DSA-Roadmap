# Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

# Alternative: Using math library
'''
import math
def factorial(n):
    return math.factorial(n)
'''

# User Input
n = int(input("\nEnter a number: "))
print(f"Factorial of {n} is :", factorial(n))