# Check if One String is Rotation of Another

# Clean Method (most efficient)
def is_rotation(s1, s2):
    """Check using concatenation trick."""
    return len(s1) == len(s2) and s2 in (s1 + s1)


# Alternative 1: Manual rotation check
def is_rotation_manual(s1, s2):
    """Check by rotating s1 step by step."""
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        rotated = s1[i:] + s1[:i]
        if rotated == s2:
            return True
    return False


# Alternative 2: Using deque rotation
from collections import deque
def is_rotation_deque(s1, s2):
    """Check using deque rotate method."""
    if len(s1) != len(s2):
        return False
    d = deque(s1)
    for _ in range(len(s1)):
        d.rotate(1)  # rotate right by 1
        if ''.join(d) == s2:
            return True
    return False


# Example Run
s1, s2 = "waterbottle", "erbottlewat"
print("Strings:", s1, "and", s2)
print("Rotation? (concat trick):", is_rotation(s1, s2))
print("Rotation? (manual check):", is_rotation_manual(s1, s2))
print("Rotation? (deque rotate):", is_rotation_deque(s1, s2))

# User Input
s1 = input("\nEnter first string: ")
s2 = input("Enter second string: ")
print("Rotation? (concat trick):", is_rotation(s1, s2))
