
# Custom style class
# You can start with a bare style class, and then set only the properties you care about.


import pygal
from pygal.style import *

x_values = list(range(11))
squares = [x**2 for x in x_values]
cubes = [x**3 for x in x_values]


chart_style = Style()
chart_style.colors = [
    '#CCCCCC', '#AAAAAA', '#888888' 
    ]

chart_style.plot_background = '#EEEEEE'

chart_style.major_label_font_size = 20
chart_style.label_font_size = 16

chart = pygal.Line(style=chart_style)
chart.force_uri_protocol = 'http'
chart.title = "Squares and Cubes"
chart.x_labels = x_values

chart.add('Squares', squares) 
chart.add('Cubes', cubes) 


chart.render_to_file('squares_cubes.svg')


