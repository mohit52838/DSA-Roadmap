# Character Frequency in String

def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

# Example Run
s = "banana"
print("String:", s)
print("Frequencies:", char_frequency(s))

# User Input
s = input("\nEnter a string: ")
print("Frequencies:", char_frequency(s))
