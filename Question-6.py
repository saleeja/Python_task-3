"""6.Write a Python program to create Fibonacci series up to n using Lambda.
Fibonacci series upto 2:
[0, 1]
Fibonacci series upto 5:
[0, 1, 1, 2, 3]
Fibonacci series upto 6:
[0, 1, 1, 2, 3, 5]
"""

# Import the 'reduce' function from the 'functools' module
from functools import reduce

# Define a lambda function 'fib_series' that generates a Fibonacci series up to 'n' elements
fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

print("Fibonacci series upto 2:")
print(fib_series(2))

print("\nFibonacci series upto 5:")
print(fib_series(5))

print("\nFibonacci series upto 6:")
print(fib_series(6))


 
   