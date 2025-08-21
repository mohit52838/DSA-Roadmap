# Reverse a String

def reverse_string(s):
    """Return the reverse of a string using slicing."""
    return s[::-1]

'''
# Alternate Approaches:

def reverse_string(s):
    # Using built-in reversed()
    return ''.join(reversed(s))

def reverse_string(s):
    # Using loop
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev
'''

# Example Run
s = "hello"
print("String:", s)
print("Reversed:", reverse_string(s))

# User Input
s = input("\nEnter a string: ")
print("Reversed:", reverse_string(s))
