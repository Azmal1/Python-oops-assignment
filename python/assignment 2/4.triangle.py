
# 4. Write a Python program to check a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with two equal sides.
# Expected Output:
# Input lengths of the triangle sides:                                    
# x: 6                                                                    
# y: 8                                                                    
# z: 12                                                                   
# Scalene triangle 

a=int(input("enter a side a:"))
b=int(input("enter a side b:"))
c=int(input("enter a side c:"))
if a==b==c:
    print("equilateral triangle")
elif a==b and a!=c or b==a and b!=c or c==a and c!=b:
    print("isosceles triangle")
else:
    print("scalene triangle")