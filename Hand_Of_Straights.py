hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]  # The list of numbers to group
groupSize = 3  # Desired size of each group
list_count = 0  # Counter for the number of valid groups formed
new_list = []  # Temporary list to build each group
counterList = []  # List to store all the formed groups

# Iterate over each number in the hand
for j in hand:
    for i in hand:  # Nested loop to check for sequential numbers
        if len(new_list) == 0:  # If new_list is empty, start a new group with the current number
            new_list.append(j)
        elif i - 1 == new_list[len(new_list) - 1]:  # Check if the current number continues the sequence
            new_list.append(i)  # Add the number to the current group
        else:
            continue  # Skip the number if it doesn't fit the sequence
        
        # Check if the group is complete
        if len(new_list) == groupSize:
            list_count += 1  # Increment the count of valid groups
            counterList.append(new_list)  # Save the completed group
            new_list = []  # Reset the group for the next iteration
            break  # Exit the inner loop once a group is completed

# Print the results
print(list_count)  # Total number of groups formed
print(counterList)  # List of all valid groups

