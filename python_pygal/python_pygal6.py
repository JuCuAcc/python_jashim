
# Parametric built-in styles
# Some built-in styles accept a custom olor, then generate a theme based on that color

import pygal
from pygal.style import LightenStyle

x_values = list(range(11))
squares = [x**2 for x in x_values]
cubes = [x**3 for x in x_values]


# Customizing individual style properties
chart_style = LightenStyle('#336688')
chart_style.plot_background = '#CCCCCC'
chart_style.major_label_font_size = 20
chart_style.label_font_size = 16


chart = pygal.Line(style=chart_style)
chart.force_uri_protocol = 'http'
chart.title = "Squares and Cubes"
chart.x_labels = x_values

chart.add('Squares', squares) 
chart.add('Cubes', cubes) 


chart.render_to_file('squares_cubes.svg')


