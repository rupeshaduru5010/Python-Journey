# Initializing a String
a = "Yo! What's happening?"
# Performing String slicing using ':'
print("Prints from the given index range :\n", a[4:])
# -> "What's happening?"
print("From one index range to another range :\n", a[4:10])
# -> "What's"
print("Prints upto given index range :\n", a[:10])
# -> "Yo! What's"
print("Prints from backwards of the sting(Dont reverse the string) :\n", a[-10:-1])
# -> "happening"
print(a[:10], a[-10:])
# -> "Yo! What's happening?"
print(a[:10] + a[-11:])
# -> "Yo! What's happening?"
