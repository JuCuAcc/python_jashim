
# Making a scatter plot
# The data for a scatter plot needs to be a list containing tuples of
# the form (x,y). THe stroke=False argument tells Pygal to make an XY
#   chart with no line connecting the points.

import pygal

squares = [
    (0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25),
    ]

chart = pygal.XY(stroke=False)
chart.force_uri_protocol = 'http'
chart.title = "Squares"
chart.add('x^2', squares) 
chart.render_to_file('squares.svg')



# List comprehension
squares = [(x, x**2) for x in range(1000)]
chart = pygal.XY(stroke=False)
chart.force_uri_protocol = 'http'
chart.title = "Squares"
chart.x_title= "Value"
chart.y_title= "Square of Value"
chart.add('x^2', squares) 
chart.render_to_file('squares.svg')



