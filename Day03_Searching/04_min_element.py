# Find Minimum Element in an Array

def find_min(arr):
    """Return minimum element in arr."""
    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val

'''
# Alternative: Using built-in min function
def find_min(arr):
    return min(arr)
'''

# Example run
arr = [12, 5, 20, 8]
print("Array:", arr)
print("Minimum element:", find_min(arr))

# User Input
n = int(input("\nEnter size of array: "))
arr = []
print("Enter elements one by one:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

print("\nArray:", arr)
print("Minimum element:", find_min(arr))