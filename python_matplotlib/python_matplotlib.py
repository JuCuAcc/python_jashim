#https://pypi.org/project/matplotlib/
#pip install matplotlib

## Making a line graph
#import matplotlib.pyplot as plt

#x_values = [0, 1, 2, 3, 4, 5]
#squares = [0, 1, 4, 9, 16, 25]

#plt.plot(x_values, squares)
#plt.show()

## Making a scatter plot
## The scatter() function takes a list of x values and a list of yvalues,
##   and avariety of optional arguments. The s=10 argument controls the size of each point.

#import matplotlib.pyplot as plt

#x_values = list(range(1000))
#squares = [x**2 for x in x_values]

#plt.scatter(x_values, squares, s=10)
#plt.show()

# Customizing plots
# Adding titles and labels, and scaling axes

import matplotlib.pyplot as plt

x_values = list(range(1000))
squares = [x**2 for x in x_values] 
#plt.scatter(x_values, squares, s=10)

# Using a colormap
# The value determine the color of each point is passed to the c argument, and
#   the cmap argument specifies which colormap to use.
# The edgecolor='none' argument removes the black outline from each point.
plt.scatter(x_values, squares, c=squares, cmap=plt.cm.Blues, edgecolor='none', s=10)
#Emphasizing points
plt.scatter(x_values[0], squares[0], c='green', edgecolor='none', s=100)
plt.scatter(x_values[-1], squares[-1], c='red', edgecolor='none', s=100)

#Removing axes
#plt.axes().get_xaxis().set_visible(False)
#plt.axes().get_yaxis().set_visible(False)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=18)
plt.ylabel("Square of Value", fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 1100, 0, 1100000]) 

# Setting a custom figure size
# The dpi argument is optional; if you don't know your system's resolution
#   you can omit the argument and adjust the figsize argument accordingly.
#plt.figure(dpi=128, figsize=(10, 6))

plt.show()

# Saving a plot
# The matplotlib viewer has an interactive save button, but you can also
# save your visualizations programmatically. To do so, replace plt.show()
#   with plt.savefig(). The bbox_inches='tight' argument trims extra
#       whitespace from the plot.

plt.savefig('squares.png', bbox_inches='tight')



