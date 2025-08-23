# Bucket Sort
def bucket_sort(arr):
    max_val = max(arr)
    size = max_val//len(arr)+1
    buckets = [[] for _ in range(size)]
    for num in arr:
        idx = min(num // size, size - 1)
        buckets[idx].append(num)
    arr = []
    for b in buckets:
        arr.extend(sorted(b))
    return arr

# Alternative: Using numpy and sort for bucket
'''
import numpy as np
def bucket_sort(arr):
    max_val = max(arr)
    size = max_val//len(arr)+1
    buckets = [[] for _ in range(size)]
    for num in arr:
        idx = min(num // size, size - 1)
        buckets[idx].append(num)
    return list(np.concatenate([sorted(b) for b in buckets]))
'''

# User Input
n = int(input("\nEnter size of array: "))
arr = []
print("Enter elements one by one:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

sorted_arr = bucket_sort(arr)
print("\nSorted Array:", sorted_arr)