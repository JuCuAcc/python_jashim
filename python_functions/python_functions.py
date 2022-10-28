

# Making a function
def greet_user():
    """Display a simple greeting"""
    print("Assalamu Alaikum!")
greet_user()

# Information that's passed to a function is called an argument;
#   information that's received by a function is called a parameter.

# Passing a single argument
def greet_user(username):
    """Display a simple greeting"""
    print("Hello, " + username + "!")
greet_user('jesse')
greet_user('diana')
greet_user('brandon')

# Using positional arguments
def describe_pet(animal, name): 
    """Display information about a pet."""
    print("\nI have a " + animal + ".")
    print("\nIt's name is " + name + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Using keyword arguments
def describe_pet(animal, name): 
    """Display information about a pet."""
    print("\nI have a " + animal + ".")
    print("\nIt's name is " + name + ".")

describe_pet(animal = 'hamster', name = 'harry')
describe_pet(name = 'willie', animal = 'dog')

# When you use keyword arguments, the order of the arguments doesn't matter.

# Parameters with default values must be listed after parameters without
#   default values in the function's definition so positional arguments
#       can still work correctly.

# Using a default value
def describe_pet(name, animal = 'dog'): 
    """Display information about a pet."""
    print("\nI have a " + animal + ".")
    print("\nIt's name is " + name + ".")

describe_pet('harry', 'hamster')
describe_pet('willie')

# Using None to make an argument optional
def describe_pet(animal, name = None): 
    """Display information about a pet."""
    print("\nI have a " + animal + ".")
    if name:
        print("\nIt's name is " + name + ".")

describe_pet('hamster', 'harry')
describe_pet('snake')

# Returning a single value
def get_full_name(first, last):
    """Return a neatly formatted full name."""
    full_name = first + ' ' + last
    return full_name.title()

musician = get_full_name('jimi', 'hendrix')
print(musician)

# Returning a dictionary
def build_person(first, last):
    """Return a dictionary of information about a person."""
    person = {'first': first, 'last':last}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)

# Returning a dictionary with optional values
def build_person(first, last, age = None):
    """Return a dictionary of information about a person."""
    person = {'first': first, 'last':last}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', 27)
print(musician)

musician = build_person('janis', 'joplin')
print(musician)


# Visualizing functions
#pythontutor.com

