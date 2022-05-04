'''
###########
Lab 5.01
###########

Instructions
------------
Write a program that uses a dictionary to offer users the meanings of common internet abbreviations.
The program, dictionary_lab.py, prompts the user to enter an internet abbreviation they would like explained. 
If the requested abbreviation is in the program's dictionary (use the in keyword with an if statement 
to test this), then it prints out the definition. If the abbreviation is not in the dictionary, the program 
prints an apologetic message saying that it could not find a definition.

Example Output:
---------------
>>> python3 dictionary_lab.py

What word would you like to look up? nbd
nbd: a phrase meaning no big deal

What word would you like to look up? kittens
Sorry, kittens is not defined

What would would you like to look up?

Bonus
------
Extend the program with any of these features:
The user can
update the definitions (values) for existing abbreviations in the dictionary
add new abbreviations (keys) and provide their definitions (values).
delete entries (key, value pairs) from the dictionary.
get the entire dictionary printed to the screen.
Lesson 6.01 did not cover all the techniques for manipulating dictionaries that you will need to program these features. Search for the necessary information in the [Python tutorial about dictionaries][1] and the [advanced Python documentation about dictionaries][2].
'''


internet_phrase_dictionary = {
'abt':'a phrase meaning about',
'bbl':'a phrase meaning be back later',
'btw':'a phrase meaning by the way',
'omg':'a phrase meaning oh my god',
'brb':'a phrase meaning be right back',
'lmk':'a phrase meaning let me know',
'ama':'a phrase meaning ask me anything',
'idc':'a phrase meaning I dont care',
'tbh':'a phrase meaning to be honest',
'tba':'a phrase meaning to be announced',
'nvm':'a phrase meaning never mind',
'imo':'a phrase meaning in my opinion',
'brb':'a phrase meaning be right back',
'nbd':'a phrase meaning no big deal',
'thx':'a phrase meaning thanks'
}
# Let's the user manipulate the dictionary internet_phrase_dictionary
def dictionary_lab():
    global internet_phrase_dictionary
    user_action = int(input("What would you like to do? Enter 1 to look up a word, 2 to update the definitions, 3 to add new abbreviations and their definitions, 4 to delete entries, and 5 to print the entire dictionary: "))
    if user_action == 1:
        user_input = ''
        while user_input != 'quit':
            user_input = input("What word would you like to look up? ")
            if user_input in internet_phrase_dictionary:
                print(internet_phrase_dictionary[user_input])
            elif user_input == 'quit':
                print("Bye!")
                break
            else:    
                print(f"Sorry, {user_input} is not defined")
    elif user_action == 2:
        which_abbr = input("Which abbreviation would you like to change the definition for? ")
        new_def = input("What would you like to change the definition to? ")
        internet_phrase_dictionary[which_abbr] = new_def
        print(internet_phrase_dictionary)
    elif user_action == 3:
        abbreviation = input("Enter your abbreviation: ")
        definition = input("Enter your definition: ")
        new_entry = {abbreviation:definition}
        internet_phrase_dictionary.update(new_entry)
        print(internet_phrase_dictionary)
    elif user_action == 4:
        key_to_delete = input("Which abbrevtiation would you like to delete? ")
        del internet_phrase_dictionary[key_to_delete]
        print(internet_phrase_dictionary)
    elif user_action == 5:
        print(internet_phrase_dictionary)
    else:
        print("Not a valid entry")
dictionary_lab()









