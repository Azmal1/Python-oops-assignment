
# 9) Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle. 

import math

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle: "))
    circle = Circle(radius)

    print("Area of the circle:", circle.area())
    print("Perimeter of the circle:", circle.perimeter())

