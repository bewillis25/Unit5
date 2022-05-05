'''
############
Do Now 5.02
############

1. In your Console
------------------
Type the following:

my_dictionary = {
'kittens': 'cute animals'
}
my_dictionary['kittens'] = 'p. cute'
print(my_dictionary)

In your Notebook
----------------
Respond to the following:

Write down what the 2nd line does. It changes the definition of kittens from 'cute animals' to 'p. cute'


2. In your Console
------------------
my_dictionary = {}
my_dictionary['puppies'] = 'baby dogs'
print(my_dictionary)

Continue in your Notebook
-------------------------
Respond to the following prompt
Write down what the 2nd line does. It adds a word and its definintion to the dictionary

3. In your Console
my_dictionary = {
'kittens': 'cute animals',
'puppies': 'baby dogs'
}
​
my_dictionary.pop('kittens')
print(my_dictionary)
my_dictionary.pop('bunnies')
my_dictionary.pop('bunnies', None)
Continue In your Notebook
Write down what the second line does. It gives a key error since 'bunnies' isn't a key in the dictionary

What is different between my_dictionary.pop('bunnies') and my_dictionary.pop('bunnies', None)? Nothing is different between them
'''
my_dictionary = {
'kittens': 'cute animals',
'puppies': 'baby dogs'
}
my_dictionary.pop('kittens', None)
print(my_dictionary)









