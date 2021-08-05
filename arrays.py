from array import *

# Create array and traverse
my_array = array("i", [1, 2, 3, 4, 5])
for i in my_array:
    print(i)
# Access individual elements through indexes
print(my_array[1])
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
my_array.buffer_info()
# Check for number of occurrences of an element using count
my_array.count(9)
# Convert array to string
temp_str = my_array.tostring()
print(temp_str)
ints = array('i')
ints.fromstring(temp_str)
print(ints)
# Convert array to a list
my_array.tolist()
# Append a string to char array

# Slice elements from an array
print(my_array[1:4])