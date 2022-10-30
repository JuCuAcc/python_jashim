#pip install pygal
#https://www.pluralsight.com/guides/charts-in-pygal

# Making a line graph
# To view the output, open the file squares.svg in a browser

import pygal

x_values = [0, 1, 2, 3, 4, 5]
squares = [0, 1, 4, 9, 16, 25]

chart = pygal.Line()
chart.force_uri_protocol = 'http'
chart.title = "Squares"
chart.x_labels = x_values
chart.x_title= "Value"
chart.y_title= "Square of Value"
chart.add('x^2', squares) 
chart.render_to_file('squares.svg')


