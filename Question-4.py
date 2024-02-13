"""4.Write a Python program to extract year, month, date and time using Lambda.
Sample Output:
2020-01-15 09:03:32.744178
2020
1
15
09:03:32.744178
"""

# Import the 'datetime' module
from datetime import datetime

# Get the current date and time using 'datetime.datetime.now()' 
current_datetime = datetime.now()
print(current_datetime)

year = lambda x: x.year # for year
print(year(current_datetime))

month = lambda x: x.month # for month
print(month(current_datetime))

day = lambda x: x.day  # for day
print(day(current_datetime))


time_now = lambda x: x.time() #for time
print(time_now(current_datetime)) 


