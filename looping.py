print("Natural Number ")
i = 1
while i <= 10:
    print(i)
    i = i + 1


print("Number Pattern ")

# Decide the row count. (above pattern contains 5 rows)
row = 5
# start: 1
# stop: row+1 (range never include stop number in result)
# step: 1
# run loop 5 times
for i in range(1, row + 1, 1):
    # Run inner loop i+1 times
    for j in range(1, i + 1):
        print(j, end=' ')
    # empty line after each row
    print("")

print("Numbers Addition")
totalNumber = 10
sum = 0
for i in range(totalNumber+1):
    sum = sum + i
    i = i + 1
print(sum)

print("Numbers Multiple")
mul = 0
for i in range(1, totalNumber+1):
    mul = i * 2
    print(mul)

print("Display numbers from a list using loop")
numbers = [12, 75, 150, 180, 145, 525, 50]
for d in numbers:
    if d > 500:
        break
    elif d > 150:
        continue
    elif d%5 == 0:
        print(d)