# Binary to Gray using recursion
def bin_to_gray(binary, i=0, gray=""):
    if i == len(binary):
        return gray
    if i == 0:
        # MSB of Gray = MSB of Binary
        gray += binary[i]
    else:
        # Gray bit = XOR of current and previous Binary bit
        gray += str(int(binary[i-1]) ^ int(binary[i]))
    return bin_to_gray(binary, i+1, gray)

# User Input
binary = input("\nEnter a binary number: ")
gray_code = bin_to_gray(binary)
print("Gray Code:", gray_code)