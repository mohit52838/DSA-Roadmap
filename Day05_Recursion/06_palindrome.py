# Palindrome check using recursion
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# Alternative: Using string reversal
'''
def is_palindrome(s):
    return s == s[::-1]
'''

# User Input
s = input("\nEnter a string: ")
if is_palindrome(s):
    print(f"{s} is a Palindrome string")
else:
    print(f"{s} is Not Palindrome string")