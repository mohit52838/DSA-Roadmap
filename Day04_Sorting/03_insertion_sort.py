# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Alternative: Using bisect module to find insertion index
'''
import bisect
def insertion_sort(arr):
    sorted_arr = []
    for x in arr:
        bisect.insort(sorted_arr, x)
    return sorted_arr
'''

# User Input
n = int(input("\nEnter size of array: "))
arr = []
print("Enter elements one by one:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

sorted_arr = insertion_sort(arr)
print("\nSorted Array:", sorted_arr)
