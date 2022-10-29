"""Represent gas and electric cars."""

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


