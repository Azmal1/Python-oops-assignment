# 4. Write a Python script to check if a given key already exists in a dictionary. 
def key_exists(d,key):
    return key in d 
d={1:2,5:6,6:2}
key_to_check=5

if key_exists(d,key_to_check):
    print(f"the key {key_to_check} exists in th edictionary")
else:
    print(f"the key {key_to_check} does not exists in th edictionary")
