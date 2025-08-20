# Sum of Array Elements

def array_sum(arr):
    return sum(arr)

'''def array_sum(arr):
    total = 0
    for num in arr:   # loop through each element
        total += num  # add it to total
    return total
'''
'''def array_sum(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total
'''

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
