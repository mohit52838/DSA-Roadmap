# Counting Sort
def counting_sort(arr):
    max_val = max(arr)
    count = [0]*(max_val+1)
    for num in arr:
        count[num] += 1
    sorted_arr = []
    for i, c in enumerate(count):
        sorted_arr.extend([i]*c)
    return sorted_arr

# Alternative: Using collections.Counter
'''
from collections import Counter
def counting_sort(arr):
    counter = Counter(arr)
    sorted_arr = []
    for key in sorted(counter.keys()):
        sorted_arr.extend([key]*counter[key])
    return sorted_arr
'''

# User Input
n = int(input("\nEnter size of array: "))
arr = []
print("Enter elements one by one:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

sorted_arr = counting_sort(arr)
print("\nSorted Array:", sorted_arr)
