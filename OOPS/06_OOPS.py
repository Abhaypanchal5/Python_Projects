class Shape:
    def area(self):
        print("Area is not defined")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Circle area: {3.14 * self.radius ** 2}")


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print(f"Rectangle area: {self.length * self.breadth}")


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print(f"Triangle area: {0.5 * self.base * self.height}")


shapes = [Circle(7), Rectangle(4, 6), Triangle(5, 10)]

for s in shapes:
    s.area()