# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Alternative: Using min() function to pick min each iteration
'''
def selection_sort(arr):
    sorted_arr = []
    temp = arr.copy()
    while temp:
        m = min(temp)
        sorted_arr.append(m)
        temp.remove(m)
    return sorted_arr
'''

# User Input
n = int(input("\nEnter size of array: "))
arr = []
print("Enter elements one by one:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

sorted_arr = selection_sort(arr)
print("\nSorted Array:", sorted_arr)
