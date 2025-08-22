# Find Peak Element in an Array
# A peak element is greater than or equal to its neighbors

def find_peak(arr):
    """Return index of a peak element (first found)."""
    n = len(arr)
    if n == 0:
        return None
    if n == 1:
        return 0  # Only one element, it's a peak
    if arr[0] >= arr[1]:
        return 0
    if arr[n - 1] >= arr[n - 2]:
        return n - 1
    
    # Check middle elements
    for i in range(1, n - 1):
        if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
            return i
    return None  # If no peak found (shouldn't happen for valid arrays)

'''
# Alternative: Binary Search approach (O(log n))
def find_peak(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left
'''

# Example run
arr = [1, 3, 20, 4, 1, 0]
print("Array:", arr)
peak_index = find_peak(arr)
print("Peak Element:", arr[peak_index], "at index", peak_index)

# User Input
n = int(input("\nEnter size of array: "))
arr = []
print("Enter elements one by one:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

print("\nArray:", arr)
peak_index = find_peak(arr)
print("Peak Element:", arr[peak_index], "at index", peak_index)