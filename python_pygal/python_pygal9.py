
# Styling individual data points
# You can style individual data points as well. To do so, write a 
# dictionary for each data point you want to customize. A 'value'
# key is required, and other properties are optional.


import pygal

repos = [
    {
        'value': 20506,
        'color': '#3333CC',
        'xlink': 'http://djangoproject.com/',
    },
    20054,
    12607,
    11827,
    ]


chart = pygal.Bar()
chart.force_uri_protocol = 'http'
chart.x_labels = [
    'django', 'requests', 'scikit-learn', 'tornado',
    ]

chart.y_title = 'Stars'
chart.add('Python Repos', repos) 

chart.render_to_file('python_repos.svg')


