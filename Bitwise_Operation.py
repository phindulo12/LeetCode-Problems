import random

# Initialize the input numbers and parameters
nums = [2, 1, 3, 4]
newnums = []  # To store binary representations
k = 1  # Variable k (currently unused in the code)
count = 2  # Counter variable (currently unused in the code)

# Convert numbers to 4-bit binary representations and store in newnums
for i in nums:
    binary_str = bin(i)[2:]  # Convert to binary and strip the '0b' prefix
    newnums.append(binary_str.zfill(4))  # Ensure 4-bit representation

print("Initial binary numbers:", newnums)

# Select a random binary number from the list
random_index = random.randint(0, len(newnums) - 1)  # Ensure index is within range
selected_binary = newnums[random_index]

# Choose a random bit position to flip
bit_position = random.randint(0, len(selected_binary) - 1)  # Ensure position is within binary string length

# Remove the selected binary number from the list
newnums.remove(selected_binary)

# Convert the binary string into a list for manipulation
intermediate_list = list(selected_binary)

# Flip the bit at the chosen position
if intermediate_list[bit_position] == "0":
    intermediate_list[bit_position] = "1"
else:
    intermediate_list[bit_position] = "0"

# Reconstruct the binary string from the modified list
modified_binary = ''.join(intermediate_list)

# Append the modified binary back to the list
newnums.append(modified_binary)

print("Modified binary numbers:", newnums)

    



