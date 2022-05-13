'''
###############
#  Lab 5.03   #
###############
In this lab your job is to create a week-long to-do list using a Python dictionary. 
Each key in the dictionary is a day of the week. Each associated value is a list of items to do that day.

The program repeatedly asks the user what action they wish to take ( add or get).

If the user enters get, the program asks for a day of the week, and then returns the to-do list for that day.

If the user enters add, the program asks for a day of the week, then asks for a new item, then adds it to the 
specified list.

If a user tries to add an item that already exists on the list for that day, the program rejects the request.

At the start of the program the dictionary should be totally empty (containing no keys and no values).

---------
-Example-
---------
Here's an example. The program output is shown in bold text, the user input in regular text. (use your imagination)

>>>python3 daily_to_do_list.py
What would you like to do ('add' or 'get')?
add
What day?
Friday
What would you like to add to Fridays to-do list?
practice clarinet
What would you like to do ('add' or 'get')?
get
What day?
Friday
You have to practice clarinet.
What would you like to do('add' or 'get')?

-------
-Bonus-
-------
It's a bit tedious for the user to have to type in three different lines to add an item to a to-do list. 
Use split() to allow the user to input add Friday watch tv and relax.  Create a variation of the program 
that doesn't allow any duplicates across any of the days. Make sure when you add a to-do item that it 
doesn't exist in the to-do lists of any of the days before adding.
'''



to_do_list = {
'Monday':[],
'Tuesday':[],
'Wednesday':[],
'Thursday':[],
'Friday':[],
'Saturday':[],
'Sunday':[]
}
# Version 1
def daily_to_do_list():
    global to_do_list
    while 1 < 2:
        action = input('What would you like to do (add or get)? ')
        day = input('What day? ')
        if day in to_do_list and action == 'add' or 'get':
            if action == 'add':
                action_on_list = input(f"What would you like to add to {day}'s to-do list? ")
                to_do_list[day].append(action_on_list)
            elif action == 'get':
                print(*to_do_list[day], sep = ", ")
            else:
                print("Not a valid action")
        elif day not in to_do_list:
            print("Not a valid day")
        elif action != 'add' or 'get':
            print("Not a valid action")
daily_to_do_list()


# Bonus Version
def bonus_to_do_list():
    global to_do_list
    while 1 < 2:
        user_data = input("Enter the action, day, and activites: ")
        user_data = user_data.split()
        action_list = user_data[2:]
        if user_data[0] == 'add':
            to_do_list[user_data[1]].append(action_list)
        elif user_data[0] == 'get':
            for i in range(0,len(to_do_list[user_data[1]])):
                a = to_do_list[user_data[1]][i]
                print(*a, sep = ' ')
bonus_to_do_list()

# No repeating bonus version
def new_bonus_to_do_list():
    global to_do_list
    while 1 < 2:
        user_data = input("Enter the action, day, and activites: ")
        user_data = user_data.split()
        action_list = user_data[2:]
        if user_data[0] == 'add':
            if action_list in to_do_list['Monday'] or to_do_list['Tuesday'] or to_do_list['Wednesday'] or to_do_list['Thursday'] or to_do_list['Friday'] or to_do_list['Saturday'] or to_do_list['Sunday']:
                print("Already in another day's list")
            else:
                to_do_list[user_data[1]].append(action_list)
        elif user_data[0] == 'get':
            for i in range(0,len(to_do_list[user_data[1]])):
                a = to_do_list[user_data[1]][i]
                print(*a, sep = ' ')
new_bonus_to_do_list()        











