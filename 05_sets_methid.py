# Creating an empty set
b = set()
print(type(b))

# Adding values to an empty set
b.add(4)
b.add(5)
b.add(5) #Adding a value repeatadly does not changes a set
b.add(9)
b.add((1,2,3)) #tuple can be add into sets

# Accesing elements
# b.add({4:5}) #can not add list or dictionary to sets
print(b)

# length of the set
print(len(b)) #Prints the length of the set

# remove of an item
b.remove(9) #Remove 9 from the set b
# b.remove(15) # Throws that error which number is not present into set
print(b)

print(b.pop())
print(b)

b.clear()
print(b)