sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

for d in sample_dict:
    if d == "city":
        print(sample_dict[d])
        sample_dict.pop(d)
        break

print(sample_dict)
sample_dict["location"] = "New york"
print(sample_dict)