"""9.Write a Python program to find the maximum value in a given heterogeneous list using lambda.Original list:
['Python', 3, 2, 4, 5, 'version']
Maximum values in the said list using lambda:5
"""



heterogeneous_list = ['Python', 3, 2, 4, 5, 'version']

# Find the maximum value using lambda, sorting by type and value
max_value = max(heterogeneous_list, key=lambda x: x if isinstance(x, (int, float)) else 0)

print("Maximum value in the list:", max_value)
