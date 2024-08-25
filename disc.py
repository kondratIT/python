#Dicts are main data type
# {"key":"value"}
#json into dict

empty_dict = dict()
empty_dict = {}

sample_dict = {"a":1, "b":2, "c":"xyz","d":["abc","cba"], "dict2":{"key1":"value1"}}

print(sample_dict)
print(sample_dict["dict2"]["key1"])
print(sample_dict["d"][0])
print(sample_dict["b"])

print(sample_dict.get("a"))
print(sample_dict.get("key1"))
print("c" in sample_dict)
print("key1" in sample_dict)
print("xyz" in sample_dict.values())
print("value1" in sample_dict.values())

for item in sample_dict:
    print(f"Key is {item} and value is {sample_dict[item]}")

print(sample_dict.items())

for k,v in sample_dict.items():
    print(f"Key is {k} and value is {v} type is {type(v)}")

d1={"key1":{"a","b","c"}}
print(d1)
print(type(d1))
print(type(d1["key1"]))

sample_dict["new key"]="new value"      #add value to dictionary
print(sample_dict)
del sample_dict["new key"]              #delete value from dictionary
print(sample_dict)






