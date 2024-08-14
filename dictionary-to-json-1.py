import json

data = {"key1": "value1", "key2": "value2"}

jsonData = json.dumps(data)
print(jsonData)

dictdata = json.loads(jsonData)
print(dictdata["key2"])
