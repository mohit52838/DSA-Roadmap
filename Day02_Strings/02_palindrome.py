# Check if a String is Palindrome

def is_palindrome(s):
    """Check if the given string is a palindrome (same forwards and backwards)."""
    return s == s[::-1]

'''
# Alternate Approach: Two-pointer method

def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
'''

# Example Run
s = "madam"
print("String:", s)
print("Palindrome?", is_palindrome(s))

# User Input
s = input("\nEnter a string: ")
print("Palindrome?", is_palindrome(s))
