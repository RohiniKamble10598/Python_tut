myDict = {
    "pankha": "fan",
    "daba": "box",
    "vastu": "Item"
}

print("options are:", myDict.keys())
a = input("enter the hindi Word \n")
# print("Meaning of your word is :", myDict[a])

# Below line will not throw error word is not in dictionary
print("Meaning of your word is :", myDict.get(a))