'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''

class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

    def perimeter(self):
        return 2 * (self.l + self.w)


length = float(input("Please provide the length of the rectangle: "))
width = float(input("Please provide the width of the rectangle: "))

print(Rectangle.area(Rectangle(length, width)))
print(Rectangle.perimeter(Rectangle(length, width)))

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * radius**2

    def circumference(self):
        return 2 * pi * radius


pi = 3.14

radius = float(input("Please provide the radius: "))

print(Circle.area(Circle(radius)))
print(Circle.circumference(Circle(radius)))











