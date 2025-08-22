# Last Occurrence of an Element

def last_occurrence(arr, target):
    """Return index of last occurrence of target in arr, -1 if not found."""
    last_idx = -1
    for i in range(len(arr)):
        if arr[i] == target:
            last_idx = i
    return last_idx

'''
# Alternative: Using reversed list with index
def last_occurrence(arr, target):
    try:
        return len(arr) - 1 - arr[::-1].index(target)
    except ValueError:
        return -1
'''

# Example run
arr = [1, 2, 3, 2, 4]
target = 2
print("Array:", arr)
print("Target:", target)
print("Last occurrence index:", last_occurrence(arr, target))

# User Input
n = int(input("\nEnter size of array: "))
arr = []
print("Enter elements one by one:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

print("\nArray:", arr)
target = int(input("Enter target element: "))
print("Last occurrence index:", last_occurrence(arr, target))