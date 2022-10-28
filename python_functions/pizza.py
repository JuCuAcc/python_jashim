# Modules

"""
    You can store your functions in aseparate file called a module,
    and then import the functions you need into the file containing
    your main program. This allows for cleaner program files.
    (Make sure your module is stored in the same directory as your main program.)
"""

def make_pizza(size, *toppings):
    """Make a pizza."""
    print("\nMaking a " + size + " pizza.")
    print("Toppings: ")
    for topping in toppings:
        print("- " + topping)
