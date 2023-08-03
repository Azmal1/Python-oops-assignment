# 14. Write a Python program to check a dictionary is empty or not. 
def empty_dict(d):
    return not bool(d)
d={}
d1={'a':1}
res=empty_dict(d)
res1=empty_dict(d1)
print(res)
print(res1) 

