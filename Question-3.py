"""3.Write a Python program to find if a given string starts with a given character using Lambda."""

# Lambda function to check if a string starts with a given character
starts_with = lambda string, char: True if string.startswith(char) else False

string = input("Enter a string: ")
character = input("Enter a character to check if the string starts with: ")

result = starts_with(string, character)

if result:
    print(f"The string starts with the character '{character}'")
else:
    print(f"The string does not start with the character '{character}'")



