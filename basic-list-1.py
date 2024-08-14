a = [30, 4, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
## print element less than 5
for data in a:
    if data < 5:
        print(data)
        b.append(data)   ### adding in a new list

b.sort()
print(b) ## print the list


number = int(input("number - "))
print(number)
for num in a:
    if num < number:
        print(num)
        break


def missing_card(cards):
    r = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    c = {"S", "H", "D", "C"}
    data = []

    for i in c:
        for j in r:
            strd = i + j
            data.append(strd)
    # print(data)

    x = cards.split(" ")
    strd = ""
    # print(x)
    for i in data:
        if i not in x:
            strd = i
            print(strd)
    return strd


print(
    missing_card(
        "S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK SA "
        "H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK HA "
        "D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK DA "
        "C2 C3 C4 C5 C6 C7 C8 C9 C10 CJ CQ CK"
    )
)
