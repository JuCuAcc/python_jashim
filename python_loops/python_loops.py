

#car = 'bmw'
#print(car == 'bmw')
#car = 'audi'
#print(car == 'bmw')
#print(car.lower() == 'audi')

#topping = 'mushrooms'
#print(topping != 'anchovies')

## Equality, Inequality and Comparison Operators
#age = 18
#age == 18
#age != 18
#age = 19
#age < 21
#age <= 21
#age > 21
#age >= 21

## Multiple conditions
#age_0 = 22
#age_1 = 18

#print(age_0 >= 21 and age_1 >= 21)
#age_1 = 23
#print(age_0 >= 21 and age_1 >= 21)

#print(age_0 >= 21 or age_1 >= 21)
#age_1 = 18
#print(age_0 >= 21 or age_1 >= 21)

## Boolean

#game_active = True
#can_edit = False


## If statement

#age = 19
#if age >= 18:
#    print("You're old enough to vote!")

#age = 17
#if age >= 18:
#    print("You're old enough to vote!")
#else:
#    print("You can't vote yet.")


#age = 12
#if age < 4:
#    price = 0
#elif age < 18:
#    price = 5
#else:
#    price = 10

#print("Your cost is $" + str(price) + ".")


#players = ['al', 'bea', 'cyn', 'dale']
#print('al' in players)
#print('eric' in players)

#banned_users = ['and', 'chad', 'dee']
#user = 'erin'

#if user not in banned_users:
#    print("You can play!")


#players = []

#if players:
#    for player in players:
#        print("Player: " + player.title())

#else:
#    print("We have no players yet!")

## Accepting input

#name = input("What's your name? ")
#print("Hello, " + name + ".")
#age = input("How old are you? ")
#age = int(age)

#if age >= 18:
#    print("\nYou can vote!")
#else:
#    print("\nYou can't vote yet.")

##Python 2.7
#name = raw_input("What's your name? ")
#print("Hello, " + name + ".")


## While loops

#current_number = 1
#while current_number <= 5: 
#    print(current_number) 
#    current_number += 1


## Letting the user choose when to quit

#prompt = "\nTell me something, and I'll "
#prompt += "repeat it back to you."
#prompt += "\nEnter 'quit' to end the program. "

#message = ""
#while message != 'quit':
#    message = input(prompt)

#    if message != 'quit':
#        print(message)

## Using a flag
#active = True
#while active:
#    message = input(prompt)

#    if message == 'quit':
#        active = False
#    else:
#        print(message)

# Using break to exit a loop
prompt = "\nWhat cities have you visited?"
prompt += "\nEnter 'quit' when you're done."

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I've been to " + city + "!")

# You can use continue to skip over certain items
#   when looping through a list or dictionary as well.

banned_users = ['eve', 'fred', 'gary', 'helen']

prompt = "\nAdd a player to your team."
prompt += "\nEnter 'quit' when you're done. "

players = []
while True: 
    player = input(prompt)
    if player == 'quit':
        break
    elif player in banned_users:    
        print(player + " is banned!")
        continue
    else:
        players.append(player)

print("\nYour team:")
for player in players:
    print(player)

## An infinite loop
#while True:
#    name = input("\nWho are you?")
#    print("Nice to meet you, " + name + "!")


# The remove() method removes a specific value from a list,
#   but it only removes the first instance of the value you provide.
#       You can use a while loop to remove all instances of a particular value.

# Removing all cats from a list of pets
pets = ['dog', 'cat', 'dog', 'fish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)