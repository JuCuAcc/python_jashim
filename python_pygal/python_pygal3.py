
# Making a bar graph
# A bar graph requires a list of values for the bar sizes.
# To label the bars, pass a list of the same length to x_labels.

import pygal


outcomes = [1, 2, 3, 4, 5, 6]
frequencies = [18, 16, 18, 17, 18, 13]

chart = pygal.Bar()
chart.force_uri_protocol = 'http'
chart.x_labels = outcomes
chart.add('D6', frequencies) 
chart.render_to_file('rolling_dice.svg')



# Making a bar graph from a dictionary
# The keys are used as the labels along the x-axis, and the values are used to 
#   determine the height of each bar.

import pygal

results = {
    1:18, 2:16, 3:18,
    4:17, 5:18, 6:13,   
    }

chart = pygal.Bar()
chart.force_uri_protocol = 'http'
chart.x_labels = results.keys()
chart.add('D6', results.values()) 
chart.render_to_file('rolling_dice.svg')


