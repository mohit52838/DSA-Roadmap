# Sum of digits using recursion
def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

# Alternative: Using while loop
'''
def sum_of_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
'''

# User Input
n = int(input("\nEnter a number: "))
print("Sum of Digits of", n, "is :", sum_of_digits(n))