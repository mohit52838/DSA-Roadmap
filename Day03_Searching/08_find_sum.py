# Sum of All Elements in an Array

def array_sum(arr):
    """Return sum of all elements in arr."""
    total = 0
    for num in arr:
        total += num
    return total

'''
# Alternative: Using built-in sum()
def array_sum(arr):
    return sum(arr)
'''

# Example run
arr = [5, 10, 15, 20]
print("Array:", arr)
print("Sum:", array_sum(arr))

# User Input
n = int(input("\nEnter size of array: "))
arr = []
print("Enter elements one by one:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

print("\nArray:", arr)
print("Sum:", array_sum(arr))