
# Importing individual classes from a module
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2022)
my_beetle.fill_tank()
my_beetle.drive()

my_tesla = ElectricCar('tesla', 'model s', 2022)
my_tesla.charge()
my_tesla.drive()

# Importing an entire module
import car

my_beetle = car.Car('volkswagen', 'beetle', 2022)
my_beetle.fill_tank()
my_beetle.drive()

my_tesla = car.ElectricCar('tesla', 'model s', 2022)
my_tesla.charge()
my_tesla.drive()

# Importing all classes from a module
from car import *

my_beetle = Car('volkswagen', 'beetle', 2022)
my_beetle.fill_tank()
my_beetle.drive()

my_tesla = ElectricCar('tesla', 'model s', 2022)
my_tesla.charge()
my_tesla.drive()

## Classes in Python 2.7
## Classes should inherit from object
#class ClassName(object):
#    pass
## The Car class in Python 2.7
#class Car(object):
#    pass
## Child class __init__() method is different
#class ChildClassName(ParentClass):
#    def __init__(self):
#        super(ClassName, self).__init__()
## The ElectricCar class in Python 2.7
#class ElectricCar(Car): 
#    def __init__(self, make, model, year):
#        super(ElectricCar, self).__init__(make, model, year)

# Storing objects in a list
# Here's an example showing how to make a fleet of rental cars,
#    and make sure all the cars are ready to drive.

# A fleet of rental cars
from car import Car, ElectricCar

# MAke lists to hold a fleet of cars.
gas_fleet = [] 
electric_fleet = [] 

# Make 500 gas cars and 250 electric cars.
for _ in range(500): 
    car = Car('ford', 'focus', 2022)
    gas_fleet.append(car)
for _ in range(250): 
    ecar = ElectricCar('nissan', 'leaf', 2022)
    electric_fleet.append(ecar)

# Fill the gas cars, and charge electric cars.
for car in gas_fleet: 
    car.fill_tank()
for ecar in electric_fleet:
    ecar.charge()

print("Gas cars: ", len(gas_fleet))
print("Electric cars: ", len(electric_fleet)) 




