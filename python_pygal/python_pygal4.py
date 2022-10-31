
# Multiple plots
# Plotting squares and cubes

import pygal

x_values = list(range(11))
squares = [x**2 for x in x_values]
cubes = [x**3 for x in x_values]

chart = pygal.Line()
chart.force_uri_protocol = 'http'
chart.title = "Squares and Cubes"
chart.x_labels = x_values

# Filling the area under a data series
# Pygal allows you to fill the area under or over each series of data.
# The default is to fill from the x-axis up, but you can fill from any
#   horizontal line using the zero argument.
chart = pygal.Line(fill=True, zero=0)

chart.add('Squares', squares) 
chart.add('Cubes', cubes) 


chart.render_to_file('squares_cubes.svg')


