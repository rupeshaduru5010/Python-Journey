fruits = [
    "Apple",
    "Goa",
    "Broccoli",
    "Grapes",
    "Carrot",
    "Orange",
    "Blackberry",
    "Dragon fruit",
]

print(fruits)
# remove()   ->Requries the element exactly in the main list
fruits.remove("Broccoli")
print(fruits)
# pop(index) ->Requires the index number of the element in the list
fruits.pop(2)
print(fruits)
# pop()      ->Pops the last element of the list
fruits.pop()
print(fruits)
# del listname[index] ->Needs the index of the element
# del listname ->deletes entire list
del fruits[1]
print(fruits)
# listname.clear() -> It cleares the entire list
fruits.clear()
print(fruits)


# Output:-
