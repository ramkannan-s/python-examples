sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75,
  'science': 35
}

min_value = int(sample_dict["Physics"])

for d in sample_dict:
    if sample_dict[d] < int(min_value):
        min_value = sample_dict[d]

print(min_value)