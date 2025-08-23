# Quick Sort (Basic)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# Advanced/Alternative: In-place quicksort
'''
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr)-1
    def partition(low, high):
        pivot = arr[high]
        i = low-1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1
    if low < high:
        pi = partition(low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
    return arr
'''

# User Input
n = int(input("\nEnter size of array: "))
arr = []
print("Enter elements one by one:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

sorted_arr = quick_sort(arr)
print("\nSorted Array:", sorted_arr)
