
# 2. Write a Python program to count the number of characters (character frequency) in a string. 
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

def character_count(string):
  count={}
  for i in string:
    if i in count:
      count[i]+=1
    else:
      count[i]=1
  return count
    
string=input("enter a string:")
res=character_count(string)
print(res)

