
# Functions that are part of a class are called methods.

# Naming conventions
# In Python class names are written in CamelCase and object names are written in lowercase with underscores.
# Modules that contain classes should still be named in lowercase with underscores.

# The Car Class

class Car():
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        """Initialize car attributes."""
        self.make = make
        self.model = model
        self.year = year

        # Fuel capacity and level in gallons.
        self.fuel_capacity = 15
        self.fuel_level = 0

    def fill_tank(self):
        """Fill gas tank to capacity."""
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full.")

    def drive(self):
        """Simulate driving."""
        print("The car is moving.")

# Creating an object from a class

my_car = Car('audi', 'a4', 2022)

# Accessing attribute values
print(my_car.make)
print(my_car.model) 
print(my_car.year) 

# Calling methods
my_car.fill_tank()
my_car.drive()

# Creating multiple objects
my_car = Car('audi', 'a4', 2022)
my_old_car = Car('subaru', 'outback', 2016)
my_truck = Car('toyota', 'tacoma', 2013)


# Modifying an attribute directly
my_new_car = Car('audi', 'a4', 2022)
my_new_car.fuel_level = 5

# Writing a method to update an attribute's value
def update_fuel_level(self, new_level): 
    """Update the fuel level."""
    if new_level <= self.fuel_capacity:
        self.fuel_level = new_level
    else: 
        print("The tank can't hold that much!")

# Writing a method to increment an attribute's value
def add_fuel(self, amount): 
    """Add fuel to the tank."""
    if (self.fuel_level + amount <= self.fuel_capacity): 
        self.fuel_level += amount
        print("Added fuel.")
    else:
        print("The tank won't hold that much.")



# Class inheritance
# To inherit from another class include the name of the
#   parent class in parentheses when defining the new class.

# The __init__() method for a child class
class ElectricCar(Car): 
    """A simple model of an electric car."""

    def __init__(self, make, model, year): 
        """Initialize an electric car."""
        super().__init__(make, model, year) 

        # Attributes specific to electric cars.
        # Battery capacity in kWh
        self.battery_size = 70
        # Charge level in %
        self.charge_level = 0

# Adding new methods to the child class
class ElectricCar(Car):
    #--snip--
    def charge(self):
        """Fully charge the vehicle."""
        self.charge_level = 100
        print("The vehicle is fully charged.")

# Using child methods and parent methods

my_ecar = ElectricCar('tesla', 'model s', 2022)

my_ecar.charge()
my_ecar.drive()


# Overriding parent methods
class ElectricCar(Car):
    #--snip--
    def fill_tank(self):
        """Display an error message."""
        print("This car has no fuel tank!")

# Instances as attributes
# A class can have objects as attributes. This allows classes
#   to work together to model complex situations.

# A Battery class
class Battery():
    """A battery for an electric car."""

    def __init__(self, size = 70): 
        """Initialize battery attributes."""
        # Capacity in kWh, charge level in %.
        self.size = size
        self.charge_level = 0

    def get_range(self):
        """Return the battery's range."""
        if self.size == 70:
            return 240
        elif self.size == 85:
            return 270

# Using an instance as an attribute
class ElectricCar(Car): 
    """A simple model of an electric car."""

    def __init__(self, make, model, year): 
        """Initialize an electric car."""
        super().__init__(make, model, year) 

        # Attributes specific to electric cars.
        self.battery = Battery()

    def charge(self):
        """Fully charge the vehicle."""
        self.battery.charge_level = 100
        print("The vehicle is fully charged.")

# Using the instance
my_ecar = ElectricCar('tesla', 'model x', 2022)

my_ecar.charge()
print(my_ecar.battery.get_range())
my_ecar.drive()

# Importing classes
# Class files can get long as you add detailed information and functionality.
# To help keep your program files uncluttered, you can store your classes in
#  modules and import the classes you need into your main program.
