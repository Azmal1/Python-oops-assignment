# 1.using 3rd variable temp
x=13
y=12
temp=x
# print("the value of temp is",temp)
print("the value of x,y after swapping is ",x,y)
x=y
# print("the value of x is",x)
y=temp
# print("the value of y is ",y)
print("the value of x,y after swapping is ",x,y)




# 2.without 3rd variable
x=12
y=13
print("the value of x,y before swapping is ",x,y)
x,y=y,x
print("the value of x,y after swapping is ",x,y)
