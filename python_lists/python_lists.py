

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

#Starting with an empty list
from audioop import reverse


users = []
users.append('val')
users.append('bob')
users.append('mia')
#Inserting elements at aparticular position
users.insert(0, 'joe')
users.insert(3, 'bea')
print(users)

#Removing elements
#If you remove an item by its value,
#Python removes only the first item that has that value.

#Deleting an element by its position
del users[-1]
#Removing an element by its value
users.remove('joe')
print(users)

#If you think of the list as a stack of items,
#pop() takes an item off the top of the stack.
#By default pop() returns the last element in the list,
# but you can also pop elements from any position in the list.

#Pop the last item from a list
most_recent_user = users.pop()
print(most_recent_user)
#Pop the first item in a list
first_user = users.pop(0)
print(first_user)

#Find the length of a list
num_users = len(users)
print("We have " + str(num_users) + " users.")

#Sorting a list
#The sorted() function returns a copy of the list,
#leaving the original list unchanged.
#Lowercase and uppercase letters may affect the sort order.

#Sorting a list permanently
users.sort()
#Sorting a list permanently in reverse alphabetical order
users.sort(reverse = True)
#Sorting a list temporarily
print(sorted(users))
print(sorted(users, reverse= True))
#Reversing the order of a list
users.reverse()

#The indented block of code makes up the body of the loop,
#where you can work with each individual item.
#Any lines that are not indented run after the loop is completed.

#Printing all items in a list
for user in users:
    print(user)

#Printing a message for each item, and aseparate message afterwards
for user in users: 
    print("Welcome, " + user + "!")
print("Welcome, we're glad to see you all!")

