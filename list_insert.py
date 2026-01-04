flowers = ["Rose", "Jasmine", "Hibiscus"]
# Using append() puts the element at the end of the list
flowers.append("Cherry Blossom")
print(flowers)
# Using insert() inserts the element at the given index
flowers.insert(2, "Lilies")
print(flowers)
carnivorus_plants = ["Venus Flytrap", "Pitcher Plant"]
# Using expand() to combine two lists
flowers.extend(carnivorus_plants)
# New list is found at the end of the main list
print(flowers)
# In list we can also extend a tuple , set and dictionary items

# Output:-

# ['Rose', 'Jasmine', 'Hibiscus', 'Cherry Blossom']
# ['Rose', 'Jasmine', 'Lilies', 'Hibiscus', 'Cherry Blossom']
# ['Rose', 'Jasmine', 'Lilies', 'Hibiscus', 'Cherry Blossom', 'Venus Flytrap', 'Pitcher Plant']
