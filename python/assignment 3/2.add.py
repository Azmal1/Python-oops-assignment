# Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

def add_value(dictionary,key,value):
    dictionary[key]=value
sample_dict={0:10,1:20}
key=2
value=30
res=add_value(sample_dict,key,value)
print(sample_dict)