

##Making a list
#users = ['val', 'bob', 'mia', 'ron', 'ned']
##Getting the first element
#first_user = users[0]
##Getting the second element
#second_user = users[1]
##Getting the last element
#newest_user = users[-1]
#print(first_user,second_user,newest_user)

##Modifying individual items
#users[0] = 'valerie'
#users[-2] = 'ronald'
#print(users[0],users[-2])

##Adding an element to the end of the list
#users.append('amy')

#for user in users:
#    print(user)

##Starting with an empty list
#from audioop import reverse


#users = []
#users.append('val')
#users.append('bob')
#users.append('mia')
##Inserting elements at aparticular position
#users.insert(0, 'joe')
#users.insert(3, 'bea')
#print(users)

##Removing elements
##If you remove an item by its value,
##Python removes only the first item that has that value.

##Deleting an element by its position
#del users[-1]
##Removing an element by its value
#users.remove('joe')
#print(users)

##If you think of the list as a stack of items,
##pop() takes an item off the top of the stack.
##By default pop() returns the last element in the list,
## but you can also pop elements from any position in the list.

##Pop the last item from a list
#most_recent_user = users.pop()
#print(most_recent_user)
##Pop the first item in a list
#first_user = users.pop(0)
#print(first_user)

##Find the length of a list
#num_users = len(users)
#print("We have " + str(num_users) + " users.")

##Sorting a list
##The sorted() function returns a copy of the list,
##leaving the original list unchanged.
##Lowercase and uppercase letters may affect the sort order.

##Sorting a list permanently
#users.sort()
##Sorting a list permanently in reverse alphabetical order
#users.sort(reverse = True)
##Sorting a list temporarily
#print(sorted(users))
#print(sorted(users, reverse= True))
##Reversing the order of a list
#users.reverse()

##The indented block of code makes up the body of the loop,
##where you can work with each individual item.
##Any lines that are not indented run after the loop is completed.

##Printing all items in a list
#for user in users:
#    print(user)

##Printing a message for each item, and a separate message afterwards
#for user in users: 
#    print("Welcome, " + user + "!")
#print("Welcome, we're glad to see you all!")

##The range() function
##Printing the numbers 0 to 1000
#for number in range(1001):
#    print(number)
    
##Printing the numbers 1 to 1000
#for number in range(1, 1001):
#    print(number)
##Making a list of numbers from 1 to a million
#numbers = list(range(1, 1000001))

##Simple statistics
#ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
#youngest = min(ages)
#oldest = max(ages)
#total_years = sum(ages)
#print(youngest, oldest, total_years)

##Slicing a list
##Getting the first three items
#finishers = ['kai', 'abe', 'ada', 'gus', 'zoe']
#first_three = finishers[:3]
#middle_three = finishers[1:4]
#last_three = finishers[-3:]
#copy_of_finishers = finishers[:]
#print(copy_of_finishers)
#print(first_three, middle_three, last_three)

##List comprehensions
##To write a comprehension, define an expression for the values you want to store in the list.
##Then write a for loop to generate input values needed to make the list.

#squares = []
#for x in range(1,11):
#    square = x**2
#    squares.append(square)
#print(squares)

##Using a comprehension to generate a list of square numbers
#squares = [x**2 for x in range(1,11)]
#print(squares)

#names = ['kai', 'abe', 'ada', 'gus', 'zoe']
#upper_names = []
#for name in names:
#    upper_names.append(name.upper())
#print(upper_names)

##Using a comprehension to convert a list of names to upper case
#names = ['kai', 'abe', 'ada', 'gus', 'zoe']
#upper_names = [name.upper() for name in names]
#print(upper_names)

##Tuples
#dimensions = (800, 600)
#for dimension in dimensions:
#    print(dimension)

#dimensions = (1200, 900)
#for dimension in dimensions:
#    print(dimension)

##pythontutor.com is a great tool for seeing how Python
##keeps track of the information in a list.
##https://pythontutor.com/render.html#mode=display

#dogs = []
#dogs.append('willie')
#dogs.append('hootz')
#dogs.append('peso')
#dogs.append('goblin')

#for dog in dogs:
#    print("Hello " + dog + "!")
#print("He loves these dogs!")

#print("\nThese were my first two dogs!")
#old_dogs = dogs[:2]
#for old_dog in old_dogs:
#    print(old_dog)

#del dogs[0]
#dogs.remove('peso')
#print(dogs)

"""
    #Styling code
    #Readbility counts

    #Use four spaces per indentation level.
    #Keep lines to 79 characters or fewer.
    #Use single blank lines to group parts of program visually.
"""