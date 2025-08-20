# Sum of Array Elements

def array_sum(arr):
    return sum(arr)

# Example Run
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
