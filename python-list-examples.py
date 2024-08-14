### sum all the items in a list
a = [3, 5, 7, 16, 73, 24]
sum = 0
for d in a:
    sum = sum + d
print(sum)

### multiple
b = [3, 5, 2]
mul = 1
for d in b:
    mul = mul * d
print(mul)

### get largest number
a = [33, 5, 7, 16, 73, 24, 4]
large = a[0]
for i in range(len(a)):
    if a[i] > large:
        large = a[i]
print(large)

for l in a:
    if l > large:
        large = l
print(large)

small = a[0]
for s in a:
    if a[i] < small:
        small = a[i]
print(small)

c = ['abc', 'xyz', 'aba', '1221']
count = 0
for i in c:
    if i[0] == i[-1]:
        count += 1
print(count)

## remove duplicates
a = [33, 5, 7, 16, 73, 7, 4]
print("The original list is : "+ str(a))
# using set() to remove duplicated from list
test_list = list(set(a))
# printing list after removal
print("The list after removing duplicates : "+ str(test_list))

non_dup = []
for i in a:
    if i not in non_dup:
        non_dup.append(i)
print(non_dup)

li = [2, 0, 2, 2]
li.append(7)
print(li)
li.insert(0, 1)
print(li)
li.insert(1, 20)
print(li)
li.insert(20, 0)
print(li)

stri = "Move#Hash#to#Front"
newstr = stri.replace('#', '')
print(newstr)
for i in stri:
    if i == "#":
        newstr = i + newstr
print(newstr)

x = stri.count("#")
stri = stri.replace("#", "")
print("#" * x + stri)