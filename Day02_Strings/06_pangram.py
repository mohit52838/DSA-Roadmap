# Check if String is a Pangram

import string

def is_pangram(s):
    """Check if a string is a pangram.
    A pangram contains every letter of the alphabet at least once.
    """
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(s.lower())

'''
def is_pangram(s):
    """Alternate method using all()"""
    s = s.lower()
    return all(ch in s for ch in string.ascii_lowercase)
'''

# Example Run
s = "The quick brown fox jumps over the lazy dog"
print("String:", s)
print("Pangram?", is_pangram(s))

# User Input
s = input("\nEnter a string: ")
print("Pangram?", is_pangram(s))
