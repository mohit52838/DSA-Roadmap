# Check if Two Strings are Anagrams

def is_anagram(s1, s2):
    """Check if two strings are anagrams.
    Returns True if they are, False otherwise.
    """
    return sorted(s1) == sorted(s2)

'''
# Alternate Approach: Using a frequency dictionary (better for large strings)

def is_anagram(s1, s2):
    freq = {}
    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s2:
        freq[ch] = freq.get(ch, 0) - 1
    return all(val == 0 for val in freq.values())
'''

# Example Run
s1, s2 = "listen", "silent"
print("Strings:", s1, "and", s2)
print("Anagram?", is_anagram(s1, s2))

# User Input
s1 = input("\nEnter first string: ")
s2 = input("Enter second string: ")
print("Anagram?", is_anagram(s1, s2))
