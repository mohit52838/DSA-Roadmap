# Reverse an Array

def reverse_array(arr):
    return arr[::-1]

# Example Run
arr = [1, 2, 3, 4, 5]
print("Original:", arr)
print("Reversed:", reverse_array(arr))

# User Input
n = int(input("\nEnter size of array: "))
arr = []
print("Enter elements one by one:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

print("\nOriginal:", arr)
print("Reversed:", reverse_array(arr))