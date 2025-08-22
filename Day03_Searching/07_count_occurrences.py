# Count Occurrences of an Element

def count_occurrences(arr, target):
    """Return how many times target occurs in arr."""
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count

'''
# Alternative: Using list.count()
def count_occurrences(arr, target):
    return arr.count(target)
'''

# Example run
arr = [1, 2, 3, 2, 4, 2]
target = 2
print("Array:", arr)
print("Target:", target)
print("Occurrences:", count_occurrences(arr, target))

# User Input
n = int(input("\nEnter size of array: "))
arr = []
print("Enter elements one by one:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

print("\nArray:", arr)
target = int(input("Enter target element: "))
print("Occurrences:", count_occurrences(arr, target))
