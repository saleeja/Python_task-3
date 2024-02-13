"""6.Write a Python program to create Fibonacci series up to n using Lambda.
Fibonacci series upto 2:
[0, 1]
Fibonacci series upto 5:
[0, 1, 1, 2, 3]
Fibonacci series upto 6:
[0, 1, 1, 2, 3, 5]
"""

from functools import reduce
fibonacci_series = lambda n: reduce(lambda x, _: x + [x[-2] + x[-1]], range(n - 2), [0, 1] if n > 1 else [0][:n])

# Example usage
n1 = 2
print(f"Fibonacci series upto {n1}: {fibonacci_series(n1)}")

n2 = 5
print(f"Fibonacci series upto {n2}: {fibonacci_series(n2)}")

n3 = 6
print(f"Fibonacci series upto {n3}: {fibonacci_series(n3)}")    