# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    data = 0
    # Implement your solution here
    max_value = max(A)
    min_value = min(A)

    for i in range(min_value, max_value):

        if i not in A and int(i) > 0:
            data = int(i)
        elif int(i) > 0:
            data = int(max_value + 1)
        else:
            data = 1

    # print(data)
    return data
    # pass
