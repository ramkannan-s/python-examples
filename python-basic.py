import sys
import datetime

print("python version")
print(sys.version)
print("Version info")
print(sys.version_info)

print(datetime.datetime.utcnow())
now = datetime.datetime.now()
print(now)

r = 1.1
areaofcircle = 3.14 * r * r
print(areaofcircle)

#sampledata = input()
sampledata = "3,4,5,2"
list = sampledata.split(",")
tuple = tuple(list)
print('List : ', list)
print('Tuple : ', tuple)

color_list = ["Red","Green","White","Black"]
for i in range(len(color_list)):
    if i == 0:
        print(color_list[i])
    if i == (len(color_list) - 1):
        print(color_list[i])

n = 5
val1 = str(n)
val2 = str(n) + str(n)
val3 = str(n) + str(n) + str(n)
print(int(val1) + int(val2) + int(val3))

# Print the docstring (documentation) of the 'abs' function
#print(abs.__doc__)
print(sys.__doc__)


print(f"test data")  ## debug print

""" Multi-line comment used
print("Python Comments") """

print("Mathematics")

lista = [8, 99, 2, 4]
for i in lista:
    diff = int(i) - 17
    print("diff value", diff)
    if diff > 17:
        mul = diff * 2
        print("multiple value", mul)


text = "IeEmpty"
if len(text) >= 2 and text[:2] == "Is":
    print(text)

s = "tpo"
stra = ""
for i in s:
    #print(i)
    stra = i + stra
print(stra)



def is_prime (n):

    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    print(n)
    return True

c = 0
for n in range(1, 1000):
    x = is_prime(n)
    c += x

print ("Total number of prime numbers present in the range: ", c)

def swap_case(s):
    string = ""
    for i in s:
        if i.isupper() == True:
            string+=(i.lower())
        else:
            string+=(i.upper())
    return string

s = "inDia on Top"
result = swap_case(s)
print(result)