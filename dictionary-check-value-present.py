sample_dict = {'g': 100, 'b': 200, 'c': 300}

for d in sample_dict:
    print(d)
    if sample_dict[d] == 200:
        print("200 present in a dict")
    else:
        print(sample_dict[d])

myDict = {'x': 1, 'bcb': 2, 'cdc': 3, 'sdd': 4}
keyToRemove = "cc"
for d in myDict:
    if d == keyToRemove:
        myDict.pop(d)
        break
print(myDict)

my_dict1 = {'x': 500, 'y': 5874, 'z': 560, 'xs': 1, 'bcb': 2, 'cdc': 3, 'sdd': 4}
largeValue = my_dict1['x']
smallValue = my_dict1['x']
for d in my_dict1:
    if my_dict1[d] > largeValue:
        largeValue = my_dict1[d]
    if my_dict1[d] < smallValue:
        smallValue = my_dict1[d]
print(largeValue)
print(smallValue)