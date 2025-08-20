# Find Second Largest Element

def second_largest(arr):
    arr = list(set(arr))  # remove duplicates
    arr.sort()
    if len(arr) < 2:
        return None
    return arr[-2]

# Example Run
arr = [12, 35, 1, 10, 34, 1]
print("Array:", arr)
print("Second largest:", second_largest(arr))

# User Input
n = int(input("\nEnter size of array: "))
arr = []
print("Enter elements one by one:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

res = second_largest(arr)
if res is None:
    print("\nNo second largest element")
else:
    print("\nSecond largest:", res)
