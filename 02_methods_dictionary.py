# dictionary methods
myDict = {
    "fast": "In a quick manner",
    "harry": "A coder",
    "marks":[1,8,6,8],
    "anotherDict":{"harry":"player"},
    1:2
}
# Prints the keys of the dictionry
print(myDict.keys())

# type dictionary
print(type(myDict))

# print the values of dictinary
print(myDict.values())

# Print (keys,values)for all contents of the dictionary
print(myDict.items())
print(myDict)

updateDict = {
    "Ronya":"Friend",
    "Shubham":"Friend",
    "Divya":"Friend",
    "harry": "A Dancer",
}
myDict.update(updateDict) #update the dictionary by adding key-value pairs form updateDict
print(myDict)

print(myDict.get("harry")) #prints the asssociated with key harry
print(myDict["harry"]) #prints the asssociated with key harry

# the Differance between .get and []syntax dictionary
print(myDict.get("harry2")) #it return None when harry2 is not present into dictionary 
# print(myDict["harry2"]) #but its harry2 is not present into dictionary it will throws an error