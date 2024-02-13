"""2.	Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number."""

def unknown_number(n):
    return lambda x: x * n


result = unknown_number(5)
print(result(10))