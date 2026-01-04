# Creating  a List
animals = ["Lion", "Tiger", "Cheetah", "Leopard", "Cheetah"]
# Printing a List
print(animals)
# Printing length of string
print(len(animals))
# Changing the List item at particular index
animals[1] = "Fox"
print(animals)
print(len(animals))
animals[4:] = "Tiger", "Wolf"
print(animals)
print(len(animals))
# List is changeable, Ordered and allows duplicate elements

# Output:-

# ['Lion', 'Tiger', 'Cheetah', 'Leopard', 'Cheetah']
# 5
# ['Lion', 'Fox', 'Cheetah', 'Leopard', 'Cheetah']
# 5
# ['Lion', 'Fox', 'Cheetah', 'Leopard', 'Tiger', 'Wolf']
# 6
