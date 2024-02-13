"""5.Write a Python program to check whether a given string is a number or not using Lambda."""

# Lambda function to check if a string is a number
is_number = lambda s: s.isdigit()

number = input("Enter a string: ")

result = is_number( number) # Check if the string is a number using the lambda function

if result:
    print("The entered string is a number.")
else:
    print("The entered string is not a number.")
