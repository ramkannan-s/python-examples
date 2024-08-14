a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even = []
for data in a:
    if (data%2 == 0): even.append(data)

print(even)


def is_prime(n):
    if ((n % 2) == 0):
        print("False")
    elif ((n % 3) == 0):
        print("False")
    else:
        print("True")

is_prime(9)
is_prime(4)
is_prime(11)

num = 11
# If given number is greater than 1
if num > 1:
    # Iterate from 2 to n // 2
    for i in range(2, (num//2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        print((num//2)+1)
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

