"""7.Write a Python program to find palindromes in a given list of strings using Lambda"""

string_list = ["madam", "dad", "python", "malayalam", "hello", "world"]

# Filter palindromes using lambda
palindromes = list(filter(lambda x: x == x[::-1], string_list))

print("Palindromes in the list:", palindromes)
