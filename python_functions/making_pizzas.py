#import pizza

#pizza.make_pizza('medium', 'pepperoni')
#pizza.make_pizza('small', 'bacon', 'pineapple')

## Importing a specific function
#from pizza import make_pizza

#make_pizza('medium', 'pepperoni')
#make_pizza('small', 'bacon', 'pineapple')

## Giving a module an alias
#import pizza as p

#p.make_pizza('medium', 'pepperoni')
#p.make_pizza('small', 'bacon', 'pineapple')

## Giving a function an alias
#from pizza import make_pizza as mp

#mp('medium', 'pepperoni')
#mp('small', 'bacon', 'pineapple')

#Importing all functions from a module
#   It can result in naming conflicts

from pizza import *

make_pizza('medium', 'pepperoni')
make_pizza('small', 'bacon', 'pineapple')