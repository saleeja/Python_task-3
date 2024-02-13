"""Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result. """

# Lambda function to add 15 to a given number
add =lambda x: x+15
number=int(input("Enter a Number:"))
result_add= add(number)
print(result_add)

# Lambda function to multiply two arguments x and y
multiply = lambda x, y: x * y

number1=int(input("Enter a Number:"))
number2=int(input("Enter a Number:"))
result_mul= multiply(number1,number2)
print(result_mul)