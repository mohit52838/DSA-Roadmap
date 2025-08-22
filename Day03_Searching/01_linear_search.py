# Linear Search in an Array

def linear_search(arr, target):
    """Return index of target in arr using linear search, -1 if not found."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

'''
# Alternative: Using Python's built-in index (may raise ValueError)
def linear_search(arr, target):
    try:
        return arr.index(target)
    except ValueError:
        return -1
'''

# Example run
arr = [4, 2, 9, 1, 7]
target = 9
print("Array:", arr)
print("Target:", target)
print("Index found at index :", linear_search(arr, target))

# User Input
n = int(input("\nEnter size of array: "))
arr = []
print("Enter elements one by one:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

print("\nArray:", arr)
target = int(input("Enter target element: "))
print("Index found at index :", linear_search(arr, target))