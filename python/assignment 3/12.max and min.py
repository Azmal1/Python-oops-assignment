# 12. Write a Python program to get the maximum and minimum value in a dictionary. 
def max_min_dict(d):
    return max(d.values()),min(d.values())
d={1: 100, 2: 4, 3: 9, 4: 16, 5: 225}
res=max_min_dict(d)
print(res)
