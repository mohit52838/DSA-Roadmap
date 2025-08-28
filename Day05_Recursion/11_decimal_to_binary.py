# Decimal to Binary using recursion
def dec_to_bin(n):
    if n == 0:
        return ""
    return dec_to_bin(n // 2) + str(n % 2)

# User Input
n = int(input("\nEnter a decimal number: "))
binary = dec_to_bin(n)
print("Binary:", binary if binary else "0")
