# Remove Duplicate Characters from String

def remove_duplicate_chr(s):
    """Return a string with duplicates removed (preserves order)."""
    result = ""
    for ch in s:
        if ch not in result:
            result += ch
    return result


# Alternate Method (using set for faster lookup)
def remove_duplicate_chr_alt(s):
    """Return a string with duplicates removed using set (preserves order)."""
    seen = set()
    result = []
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    return ''.join(result)


# Example Run
s = "programming"
print("String:", s)
print("Without duplicates:", remove_duplicate_chr(s))

# User Input
s = input("\nEnter a string: ")
print("Without duplicates:", remove_duplicate_chr(s))
