# Find Longest Word(s) in a Sentence

def longest_words(sentence):
    """Return longest word(s). Gives one word if unique, else returns a list."""
    words = sentence.split()
    max_len = max(len(w) for w in words)   # find the maximum length
    longest = [w for w in words if len(w) == max_len]
    return longest[0] if len(longest) == 1 else longest


# Alternate Method (loop-based)
def longest_words_alt(sentence):
    """Return longest word(s) using a loop."""
    words = sentence.split()
    longest = []
    max_len = 0
    for w in words:
        if len(w) > max_len:
            longest = [w]
            max_len = len(w)
        elif len(w) == max_len:
            longest.append(w)
    return longest[0] if len(longest) == 1 else longest


# Example Run
s = "I enjoy solving coding puzzles"
print("Sentence:", s)
print("Longest word(s):", longest_words(s))

# User Input
s = input("\nEnter a sentence: ")
print("Longest word(s):", longest_words(s))
