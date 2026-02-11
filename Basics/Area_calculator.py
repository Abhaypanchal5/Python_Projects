class AreaCalculator:
    def calculate_area(self, shape):
        if shape == "C" or shape == "circle".upper():
            radius = float(input("Enter the radius of the circle: "))
            area = (22/7) * radius ** 2
            print(f"The area of the circle is: {area}")
        elif shape == "R" or shape == "rectangle".upper():
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = length * width
            print(f"The area of the rectangle is: {area}")
        elif shape == "T" or shape == "triangle".upper():
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            area = 0.5 * base * height
            print(f"The area of the triangle is: {area}")
        elif shape == "S" or shape == "square".upper():
            side = float(input("Enter the side length of the square: "))
            area = side ** 2
            print(f"The area of the square is: {area}")
        else:
            print("Invalid shape. Please choose from circle(C), rectangle(R), triangle(T), or square(S).")

n = AreaCalculator()
shape = input("Enter the shape (circle(C), rectangle(R), triangle(T), square(S)): ").upper()
n.calculate_area(shape) 

# this code defines a class `AreaCalculator` with a method `calculate_area` that calculates the area of different shapes based on user input.
# The user is prompted to enter the shape they want to calculate the area for, and then the necessary dimensions are requested to compute and display the area.
