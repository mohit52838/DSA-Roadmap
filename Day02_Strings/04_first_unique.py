# Find First Non-Repeating Character

def first_unique(s):
    """Return the first non-repeating character in the given string.
    If none exists, return None.
    """
    for ch in s:
        if s.count(ch) == 1:
            return ch
    return None

'''
# Alternate Approach: Using a frequency dictionary (more efficient for large strings)

def first_unique(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None
'''

# Example Run
s = "swiss"
print("String:", s)
print("First unique char:", first_unique(s))

# User Input
s = input("\nEnter a string: ")
result = first_unique(s)
print("First unique char:", result if result else "None")
