"""10.Create a Python module (a separate .py file) that contains a function to calculate the area of a rectangle. Then, in another Python script, import the module and use the function to calculate the area of a rectangle with specific dimensions."""
from area import calculate_area

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

area = calculate_area(length, width)

print("The area of the rectangle is:", area)
