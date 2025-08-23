# Radix Sort
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0]*n
    count = [0]*10
    for i in range(n):
        index = (arr[i]//exp) % 10
        count[index] += 1
    for i in range(1,10):
        count[i] += count[i-1]
    i = n-1
    while i >= 0:
        index = (arr[i]//exp) % 10
        output[count[index]-1] = arr[i]
        count[index] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val//exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

# Alternative: Can also use key in sorted() with string conversion
'''
def radix_sort(arr):
    max_len = len(str(max(arr)))
    for d in range(max_len):
        arr = sorted(arr, key=lambda x: (x // (10**d)) % 10)
    return arr
'''

# User Input
n = int(input("\nEnter size of array: "))
arr = []
print("Enter elements one by one:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

sorted_arr = radix_sort(arr)
print("\nSorted Array:", sorted_arr)
