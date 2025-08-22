# Average of All Elements in an Array

def array_average(arr):
    """Return average of elements in arr."""
    total = 0
    for num in arr:
        total += num
    return total / len(arr)

'''
# Alternative: Using sum()/len()
def array_average(arr):
    return sum(arr)/len(arr)
'''

# Example run
arr = [5, 10, 15, 20]
print("Array:", arr)
print("Average:", array_average(arr))

# User Input
n = int(input("\nEnter size of array: "))
arr = []
print("Enter elements one by one:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

print("\nArray:", arr)
if n == 0:
    print("Average: None")
else:
    # Calculate and print average only if the array is not empty
    print("Average:", array_average(arr))