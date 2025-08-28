# Power using recursion
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n-1)

# Alternative: Using exponentiation operator
'''
def power(x, n):
    return x ** n
'''

# User Input
x = int(input("\nEnter base: "))
n = int(input("Enter exponent: "))
print("Result:", power(x, n))