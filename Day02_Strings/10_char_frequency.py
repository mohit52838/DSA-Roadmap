# Character Frequency in String

def char_frequency(s):
    """Return character frequencies using dictionary (manual method)."""
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


# Alternate using collections.Counter
from collections import Counter
def char_frequency_alt(s):
    """Return character frequencies using Counter (shorter)."""
    return dict(Counter(s))


# Pythonic one-liner
def char_frequency_one_liner(s):
    """Return character frequencies in one line."""
    return {ch: s.count(ch) for ch in set(s)}


# Example Run
s = "banana"
print("String:", s)
print("Frequencies (manual):", char_frequency(s))
print("Frequencies (Counter):", char_frequency_alt(s))
print("Frequencies (one-liner):", char_frequency_one_liner(s))

# User Input
s = input("\nEnter a string: ")
print("Frequencies (manual):", char_frequency(s))