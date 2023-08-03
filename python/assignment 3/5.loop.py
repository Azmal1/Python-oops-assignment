# 5. Write a Python program to iterate over dictionaries using for loops.
d = {1: 2, 5: 6, 6: 2}

print("key:")
for key in d:
    print(key)

print("value:")
for value in d.values():
    print(value)

print("key:value pair:")
for key,value in d.items():
    print(f"key:{key},value:{value}")