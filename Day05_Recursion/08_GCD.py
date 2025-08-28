# Greater Common Divisor using recursion
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Alternative: Using math library
'''
import math
def gcd(a, b):
    return math.gcd(a, b)
'''

# User Input
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
print("GCD:", gcd(a, b))