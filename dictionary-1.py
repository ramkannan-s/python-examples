dicta = {"tn": "chennai", "ka": "begaluru", "ap": "hyderabad", "kl": "ernakulam"}
print(dicta)
print(dicta.get("tn"))
print(dicta.keys())
print(dicta.values())

for data in dicta:
    value = dicta[data]
    print("for state " + data.upper() +" the capital is " + value)

s = "w3resource"
dictb = {}
for i, idx in enumerate(s):
    print(i, idx)
    dictb[idx] = i
print(dictb)