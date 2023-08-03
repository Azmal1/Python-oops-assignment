#  Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result.
#  Sample Output: 25 48 
add_15= lambda x:x+15
multiply= lambda x, y:x*y

num1=10
res1=add_15(num1)
print(res1)

num2=10 
num3=20
res2=multiply(num2,num3)
print(res2)