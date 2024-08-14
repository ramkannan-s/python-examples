# demo is the function name
def demo(name, age):
    # print value
    print(name, age)


# call function
demo("Ben", 25)


def func1(*args):
    for i in args:
        print(i)


func1(20, 40, 60)
func1(80, 100)


def calculate(a, b):
    sum = a + b
    sub = a - b
    return sum, sub


add, sub = calculate(49, 5)
print(add, sub)

# function with default argument
def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)

show_employee("Ben", 12000)
show_employee("Jessa")


# This function returns a tuple
def fun():
    str = "geeksforgeeks"
    x = 20
    return str, x  # Return tuple, we could also
    # write (str, x)


# Driver code to test above method
str, x = fun()  # Assign returned tuple
print(str)
print(x)