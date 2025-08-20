# Linear Search

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return print("Not found")

# Example Run
arr = [4, 2, 9, 1, 7]
print("Array:", arr)
print("Index of 9:", linear_search(arr, 9))
print("Index of 5:", linear_search(arr, 5))

# User Input
n = int(input("\nEnter size of array: "))
arr = []
print("Enter elements one by one:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

target = int(input("\nEnter element to search: "))
idx = linear_search(arr, target)
if idx != -1:
    print(f"Element found at index {idx}")
else:
    print("Element not found")
