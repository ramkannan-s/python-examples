print("Hello World !")

a = 1
b = 2
sum = a + b
print(sum)

odd_or_even_number = 12

if odd_or_even_number > 1:
    if odd_or_even_number % 2 == 0:
        print("Even")
    else:
        print("Odd")

factorial_num = 5

x = 1
y = 2
z = 2
listlargest = []
listlargest.append(x)
listlargest.append(y)
listlargest.append(z)
large = listlargest[0]

for i in listlargest:
    if i > large:
        large = i
print(large)
