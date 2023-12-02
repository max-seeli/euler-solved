# Problem: 19
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

import datetime

count = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if datetime.date(year, month, 1).weekday() == 6:
            count += 1
print(count)

# Alternative without datetime module

count = 0
weekday = 2
for year in range(1901, 2001):
    for month in range(1, 13):
        if weekday == 0:
            count += 1
        if month == 4 or month == 6 or month == 9 or month == 11:
            weekday = (weekday + 2) % 7
        elif month == 2:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                weekday = (weekday + 1) % 7
        else:
            weekday = (weekday + 3) % 7
print(count)
