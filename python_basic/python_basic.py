
##Initial

#print("Jashim Uddin")
#msg = "Assalamu Alaikum"
#print(msg)
#first_name = "Jashim"
#last_name = "Uddin"
#full_name = first_name + ' ' + last_name
#print(full_name)

##Lists
#bikes = ['trek', 'redline', 'giant']
#first_bike = bikes[0]
#last_bike = bikes[-1]
#print(first_bike)
#print(last_bike)

##Looping through list
#for bike in bikes:
#    print(bike)

#bikes = []
#bikes.append('trek')
#bikes.append('redline')
#bikes.append('giant')

##Looping through list
#for bike in bikes:
#    print(bike)

##Making numerical lists
#squares = []
#for x in range(1,11):
#    squares.append(x**2)
#print(squares)

##List Comprehensions
#squares = [x**2 for x in range(1,11)]
#for square in squares:
#    print(square)

##Slicing a list
#finishers = ['sam', 'bob', 'ada', 'bea']
#first_two = finishers[:2]
#print(first_two)

##Copying a list
#bikes = ['trek', 'redline', 'giant']

##Boolean
#'trek' in bikes
#'surly' not in bikes 
#game_active = True
#can_edit = False

#copy_of_bikes = bikes[:]
#print(copy_of_bikes)

##Tuples are similar to lists, but the items in atuple can't be modified
##Making a tuple
#dimensions =(1920, 1080)
#print(dimensions)


##If statements
#age = 20
#if age >= 18:
#    print("You can vote!")

##if-elif-else statements
#age = 10
#if age < 4:
#    ticket_price = 0
#elif age < 18:
#    ticket_price = 10
#else:
#    ticket_price = 15
#print(ticket_price)

##Dictionaries
#alien = {'color': 'green', 'points': 5}
#print("The alien's color is " + alien['color'])
#alien['x_position'] = 0
##Looping through all key-value pairs
#fav_numbers = {'eric': 17, 'ever': 4}
#for name in fav_numbers.keys():
#    print(name + ' loves a number')
##Looping through all values
#fav_numbers = {'eric': 17, 'ever': 4}
#for number in fav_numbers.values():
#    print(str(number) + ' is a favorite')

##User input

#name = input("What's your name? \n")
#print("Hello, " + name + "!")
#age = input("How old are you? \n")
#age = int(age)
#print("You are " + str(age) + " years old. ")

#pi = input("What's the value of pi? ")
#pi = float(pi)
#print(pi)

##While loops
#current_value = 1
#while current_value <= 5:
#    print(current_value)
#    current_value += 1

## Letting user choose when to quit
#msg = ''
#while msg != 'quit':
#    msg = input("What's your message?\t")
#    print(msg)

##Functions
#def greet_user():
#    """Display a simple greeting."""
#    print("Hi!")
#greet_user()

#def greet_user(username):
#    """Display a personalized greeting."""
#    print("Hello, " + username + "!")
#greet_user('Jashim')

##Default values for parameters
#def make_pizza(topping='bacon'):
#    """Make a single-topping pizza."""
#    print("Have a " + topping + " pizza!")

#make_pizza()
#make_pizza('pepperoni')

##Returning a value
#def add_numbers(x, y):
#    """Add two numbers and return the sum."""
#    return x + y

#sum = add_numbers(3, 5)
#print(sum)

#Classes
#A class defines the behavior of an object and the kind of information an object can store.
#The information in aclass is stored in attributes, and functions that belong to a class are called methods.
#A child class inherits the attributes and methods from its parent class.

#Creating a dog class
class Dog():
    """Represent a dog."""
    def __init__(self, name):
        """Initialize dog object."""
        self.name = name
    def sit(self):
        """Simulate sitting."""
        print(self.name + " is sitting.")

my_dog = Dog('Peso')

print(my_dog.name + " is a great dog!")
my_dog.sit()


#Inheritance
class SARDog(Dog):
    """Represent a search dog."""
    def __init__(self, name):
        """Initialize the sardog."""
        super().__init__(name)
    def search(self):
        """Simulate searching."""
        print(self.name + " is searching.")

my_dog = SARDog('Willie')

print(my_dog.name + " is a search dog.")
my_dog.sit()
my_dog.search()





