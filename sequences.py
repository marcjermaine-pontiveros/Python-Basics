'''
Strings
: Ordered: Yes
Mutable: No
'''
name = "Harry"
print(name[0])
print(name[1])

'''
Lists
: Ordered: Yes
Mutable: Yes
'''

# This is a Python comment
names = ["Harry", "Ron", "Hermione"]
# Print the entire list:
print(names)
# Print the second element of the list:
print(names[1])
# Add a new name to the list:
names.append("Draco")
# Sort the list:
names.sort()
# Print the new list:
print(names)


'''
Tuples
: Ordered: Yes
Mutable: No
'''

'''
point = (12.5, 10.6)
'''

'''
Sets
: Ordered: No
'''

# Create an empty set:
s = set()

# Add some elements:
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
s.add(1)

# Remove 2 from the set
s.remove(2)

# Print the set:
print(s)

# Find the size of the set:
print(f"The set has {len(s)} elements.")

'''
Dictionaries
: Ordered: No
Mutable: Yes
'''

'''
# Define a dictionary
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
# Print out Harry's house
print(houses["Harry"])
# Adding values to a dictionary:
houses["Hermione"] = "Gryffindor"
# Print out Hermione's House:
print(houses["Hermione"])

'''