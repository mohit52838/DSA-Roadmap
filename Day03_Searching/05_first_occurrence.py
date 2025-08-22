# First Occurrence of an Element

def first_occurrence(arr, target):
    """Return index of first occurrence of target in arr, -1 if not found."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

'''
# Alternative: Using list.index() (may raise ValueError)
def first_occurrence(arr, target):
    try:
        return arr.index(target)
    except ValueError:
        return -1
'''

# Example run
arr = [1, 2, 3, 2, 4]
target = 2
print("Array:", arr)
print("Target:", target)
print("First occurrence index:", first_occurrence(arr, target))

# User Input
n = int(input("\nEnter size of array: "))
arr = []
print("Enter elements one by one:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

print("\nArray:", arr)
target = int(input("Enter target element: "))
print("First occurrence index:", first_occurrence(arr, target))