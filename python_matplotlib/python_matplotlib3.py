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

## Plotting high temperatures
## The following code creates a list of dates and a corresponding list of high temperatures.
##   It then plots the high temperatures, with the date labels displayed in aspecific format.

#from datetime import datetime as dt

#import matplotlib.pyplot as plt
#from matplotlib import dates as mdates

#dates = [
#    dt(2022, 6, 21), dt(2022, 6, 22),
#    dt(2022, 6, 23), dt(2022, 6, 24),
#    ]

#highs = [57, 68, 64, 59]

#fig = plt.figure(dpi=128, figsize=(10,6))
#plt.plot(dates, highs, c='red')
#plt.title("Daily High Temps", fontsize=24)
#plt.ylabel("Temp (F)", fontsize=16) 

#x_axis = plt.axes().get_xaxis()
#x_axis.set_major_formatter(
#    mdates.DateFormatter('%B %d %Y')
#    )
#fig.autofmt_xdate()

#plt.show()


# The plt.subplots() function returns a figure object and a tuple of axes.
# Each set of axes corresponds to a separate plot in the figure.
# The first two arguments control the number of rows and columns generated in the figure.

import matplotlib.pyplot as plt

x_vals = list(range(11))
squares = [x**2 for x in x_vals]
cubes = [x**3 for x in x_vals]

fig, axarr = plt.subplots(2, 1, sharex=True)

axarr[0].scatter(x_vals, squares)
axarr[0].set_title('Squares')

axarr[1].scatter(x_vals, cubes, c='red')
axarr[1].set_title('Cubes')

plt.show()

# Sharing a y-axis
# To share a y-axis, we use the sharey=True argument.


import matplotlib.pyplot as plt

x_vals = list(range(11))
squares = [x**2 for x in x_vals]
cubes = [x**3 for x in x_vals]

fig, axarr = plt.subplots(1, 2, sharey=True)

axarr[0].scatter(x_vals, squares)
axarr[0].set_title('Squares')

axarr[1].scatter(x_vals, cubes, c='red')
axarr[1].set_title('Cubes')

plt.show()


