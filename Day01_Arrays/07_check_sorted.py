# Check if Array is Sorted

def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

# Example Run
print("Is [1, 2, 3, 4, 5] sorted?", is_sorted([1, 2, 3, 4, 5]))
print("Is [3, 2, 1] sorted?", is_sorted([3, 2, 1]))

# User Input
n = int(input("\nEnter size of array: "))
arr = []
print("Enter elements one by one:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

print("\nArray:", arr)
print("Sorted?", is_sorted(arr))
