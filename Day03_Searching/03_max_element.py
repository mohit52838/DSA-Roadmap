# Find Maximum Element in an Array

def find_max(arr):
    """Return maximum element in arr."""
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

'''
# Alternative: Using built-in max function
def find_max(arr):
    return max(arr)
'''

# Example run
arr = [12, 5, 20, 8]
print("Array:", arr)
print("Maximum element:", find_max(arr))

# User Input
n = int(input("\nEnter size of array: "))
arr = []
print("Enter elements one by one:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))
    
print("\nArray:", arr)
print("Maximum element:", find_max(arr))