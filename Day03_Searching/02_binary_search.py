# Binary Search in a Sorted Array

def binary_search(arr, target):
    """Return index of target in sorted arr using binary search, -1 if not found."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

'''
# Alternative: Recursive binary search
def binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid+1, right)
    else:
        return binary_search(arr, target, left, mid-1)
'''

# Example run
arr = [1, 3, 5, 7, 9]
target = 7
print("Array:", arr)
print("Target:", target)
print("Index found at index :", binary_search(arr, target))

# User Input
n = int(input("\nEnter size of sorted array: "))
arr = []
print("Enter elements one by one (sorted order):")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

print("\nArray:", arr)
target = int(input("Enter target element: "))
print("Index found at index :", binary_search(arr, target))
