
#pip install pygal_maps_world

# Plotting global datasets
# Pygal can generate world maps, and you can add any data you want to these maps.
# Data is indicated by coloring, by labels, and by tooltips that show data when
# users hover over each country an the map.

# The following code makes a simple world map showing the countries of North America.
from pygal.maps.world import World

wm = World()
wm.force_uri_protocol = 'http'
wm.title = 'North America'
wm.add('North America', ['ca', 'mx', 'us'])

wm.render_to_file('north_america.svg')


# The following example will print an alphabetical list of each country and its code.
from pygal.maps.world import COUNTRIES

for code in sorted(COUNTRIES.keys()): 
    print(code, COUNTRIES[code])

# To plot numerical data on a map, pass a dictionary to add() instead of a list.
from pygal.maps.world import World

populations = {
    'ca': 34126000,
    'us': 309349000,
    'mx': 113423000,
    }


wm = World()
wm.force_uri_protocol = 'http'
wm.title = 'Population of North America'
wm.add('North America', populations)

wm.render_to_file('na_populations.svg')