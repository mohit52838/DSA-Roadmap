# Find Maximum & Minimum in Array

def find_max_min(arr):
    return max(arr), min(arr)

'''def find_max_min(arr):
    # assume first element is both max and min
    maximum = arr[0]
    minimum = arr[0]

    for num in arr:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return maximum, minimum
'''

# Example Run
arr = [7, 2, 9, 4, 1]
mx, mn = find_max_min(arr)
print("Array:", arr)
print("Max:", mx, "Min:", mn)

# User Input
n = int(input("\nEnter size of array: "))
arr = []
print("Enter elements one by one:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

mx, mn = find_max_min(arr)
print("\nArray:", arr)
print("Max:", mx, "Min:", mn)