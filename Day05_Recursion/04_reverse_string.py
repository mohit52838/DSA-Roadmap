# Reverse string using recursion
def reverse_string(s):
    if len(s) == 0:
        return ""
    return reverse_string(s[1:]) + s[0]

# Alternative: Using slicing
'''
def reverse_string(s):
    return s[::-1]
'''

# User Input
s = input("\nEnter a string: ")
print("Reversed String:", reverse_string(s))