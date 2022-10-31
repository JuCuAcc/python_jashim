
# Styling plots
# Using built-in styles
# Import the style and make an instance of the style class.
#   Then pass the style object with the style argument
#       when you make the chart object.


import pygal
from pygal.style import LightGreenStyle

x_values = list(range(11))
squares = [x**2 for x in x_values]
cubes = [x**3 for x in x_values]

chart_style = LightGreenStyle()
chart = pygal.Line(style=chart_style)
chart.force_uri_protocol = 'http'
chart.title = "Squares and Cubes"
chart.x_labels = x_values

chart.add('Squares', squares) 
chart.add('Cubes', cubes) 


chart.render_to_file('squares_cubes.svg')


