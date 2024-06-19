# Date: 18th January 2024 Thursday
# Start Time: 10 : 03 PM
# End Time: 10 : 37 PM

# Area of circle = pie r**2
# Circumference of circle = 2pie r
class Circle:
    pie = 3.14  # Class Object Attribute
    def __init__(self, radius=3):
        self.radius = radius
        self.area = Circle.pie * radius *radius
    def circumference(self):
        return 2 * Circle.pie * self.radius

circle_1 = Circle(4)
print(f"The circumference of Circle 1 is: {circle_1.circumference()}")
circle_2 = Circle(14)
print(f"The circumference of Circle 2 is: {circle_2.circumference()}")
print(f"The area of circle 1 is: {circle_1.area}")

class rectangle:
    def __init__(self, length, width):
        self.area = length * width
rectangle_1 = rectangle(5,9)
print(f"The area of rectangle is: {rectangle_1.area}")
