# Count Vowels in a String

def count_vowels(s):
    """Count the number of vowels (a, e, i, o, u) in the given string."""
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)

'''
# Alternate Approach: Using a simple loop

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count
'''

# Example Run
s = "beautiful"
print("String:", s)
print("Vowels:", count_vowels(s))

# User Input
s = input("\nEnter a string: ")
print("Vowels:", count_vowels(s))
