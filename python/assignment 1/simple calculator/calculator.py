def calculator(x,y,z):
  if z=='+':
    print(x+y)
  elif z=="-":
    print(x-y)
  elif z=='*':
    print(x*y)
  elif z=='/':
    print(x/y)
  elif z=="//":
    print(x//y)
  elif z=='%':
    print(x%y)
  elif z=='**':
    print(x**y)
  else:
    print("invalid operation")



x=int(input("enter the first number:"))
y=int(input("enter the second number:"))
z=input("enter the operation to perform:")
calculator(x,y,z)