from array import *

# Create array and tranverse
my_array = array("i", [1, 2, 3, 4, 5])
for i in my_array:
    print(i)
# Access indiviual elements through indexes
my_array[1]
# Append any value to the array
my_array.append(6)
# Insert value in an array
my_array.insert(0, 0)
# Extend array
second_array = array("i", [10, 11, 12, 13])
my_array.extend(second_array)

# Add items from list into array
temp_list = [9, 8, 7]
my_array.fromlist(temp_list)
# Remove any array element
my_array.remove(2)
# Remove last array element
my_array.pop()
# Fetch any element
my_array.index(5)
# Reverse an array
my_array.reverse()
# Get array buffer information

# Check for number of occurences of an element using count

# Convert array to string

# Convert array to a list

# Append a string to char array

# Slice elements from an array