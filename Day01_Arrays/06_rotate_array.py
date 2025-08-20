# Rotate Array by K (Right Rotation)

def rotate_array(arr, k):
    n = len(arr)
    k %= n  # handle k > n
    return arr[-k:] + arr[:-k]

# Example Run
arr = [1, 2, 3, 4, 5, 6, 7]
print("Original:", arr)
print("Rotated by 3:", rotate_array(arr, 3))

# User Input
n = int(input("\nEnter size of array: "))
arr = []
print("Enter elements one by one:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

k = int(input("\nEnter rotation value K: "))
print("Original:", arr)
print("Rotated Array:", rotate_array(arr, k))
