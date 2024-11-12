# Create an empty list called my_list
my_list = []

# Append the specified elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert the value 15 at the second position in the list
my_list.insert(1, 15)  # Index 1 is the second position

# Extend my_list with another list
my_list.extend([50, 60, 70])

# Remove the last element from my_list
my_list.pop()  # Removes the last element (70)

# Sort my_list in ascending order
my_list.sort()

# Find and print the index of the value 30 in my_list
index_30 = my_list.index(30)
print("Index of 30:", index_30)

# Optional: Print the final list
print("Final list:", my_list)