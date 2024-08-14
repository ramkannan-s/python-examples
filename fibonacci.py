FibonacciNumber = 15
n1 = 0
n2 = 1
n3 = 2
print(n1)
print(n2)

for i in range(2, FibonacciNumber):
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3


### palindrome program
x = "hsgt"

w = ""
for i in x:
    w = i + w
    print(w)

if (x == w):
    print("Yes Its Palindrome")
else:
    print("No")

#import panda as pd
#s = pd.Series([1, 2, 3, 4, 5])
#s.replace([2, 4], [6,7], inplace=True)


### list to tuple, set
l = [4, 8, 6, 4]
tupledata = tuple(l)
setdata = set(l)
print(tupledata)
print(setdata)

# List of fruits
fruits = ['apple', 'banana', 'cherry', 'apple']

# Initialize an empty dictionary
fruit_dict = {}

# Populate the dictionary using a loop
for idx, fruit in enumerate(fruits):
    fruit_dict[fruit] = idx

print(fruit_dict)

### iterate through a Python list of tuples
L = [(1, 2, "3"), (4, 5, 6), (7, 8, 9, 10)]
dictd = { 1: "a", 2: "b", 3: "c", 4: "d" }
print(dictd)
for x in L:
    print(x)
    for y in x:
        print(y)
        dictd.pop(y)
        break
    print(str(dictd))