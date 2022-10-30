## Multiple plots


### Plotting two sets of data
### The scatter() function takes a list of x values and a list of yvalues,


#import matplotlib.pyplot as plt

#x_values = list(range(11))
#squares = [x**2 for x in x_values]
#cubes = [x**3 for x in x_values]


#plt.scatter(x_values, squares, c='blue', edgecolor='none', s=20)
#plt.scatter(x_values, cubes, c='red', edgecolor='none', s=20)

## Filling the space between data sets
## The fill_between() method fills the space between two data sets.
##   It takes a series of x-values and two series of y-values. 
##   It also takes a facecolor to use for the fill, and an optional
##       alpha argument that color's transparency.
#plt.fill_between(x_values, cubes, squares, facecolor='blue', alpha=0.25)

#plt.axis([0, 11, 0, 1100])
#plt.show()

# Working with dates and times
# Pthon's datetime module helps you work with date or time value.
# The datetime.now() function returns a datetime object representing the current date and time.
from datetime import datetime as dt

today = dt.now()
date_string = dt.strftime(today, '%m/%d/%Y')
print(date_string)

new_years = dt(2023, 1, 1)
fall_equinox = dt(year=2016, month=9, day=22)

print(new_years)
print(fall_equinox)


# Datetime formatting arguments
# The strftime() function generates a formatted string from a datetime object, and
# the strptime() function generates a datetime object from a string.
# The following codes let you work with dates exactly as you need to.

"""
    %A  Weekday name, such as Monday
    %B  Month name, such as January
    %m  Month, as a number (01 to 12)
    %d  Day of the month, as a number (01 to 31)
    %Y  Four-digit year, such as 2022
    %y  Two-digit year, such as 22
    %H  Hour, in 24-hour format (00 to 23)
    %I  Hour, in 12-hour format (01 to 12)
    %p  AM or PM
    %M  Minutes (00 to 59)
    %S  Seconds (00 to 61)
"""

# Converting a string to a datetime object 
new_years = dt.strptime('1/1/2023', '%m/%d/%Y')
print(new_years)
ny_string = dt.strftime(new_years, '%B %d, %Y')
print(ny_string)


