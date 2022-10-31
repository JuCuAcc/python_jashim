
# Configuration settings
# Some settings are controlled by a Config object


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

my_config = pygal.Config()
my_config.show_y_guides = False
my_config.width = 1000
my_config.dots_size = 5

#chart = pygal.Line(style=chart_style)
#chart = pygal.Line(style=chart_style, config=my_config)
chart = pygal.Line(config=my_config)

chart.force_uri_protocol = 'http'
chart.title = "Squares and Cubes"
chart.x_labels = x_values

chart.add('Squares', squares, dots_size=2) 
chart.add('Cubes', cubes, dots_size=3) 


chart.render_to_file('squares_cubes.svg')


