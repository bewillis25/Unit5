'''
############
Do Now 5.01
############

In your Console
---------------
Type the following code:

my_dictionary = {
'cat': 'a domestic feline',
'dog': 'a domestic canine',
'chair': 'furniture piece for sitting',
'car': 'automobile'
}
print(my_dictionary)
print(my_dictionary['dog'])
print(my_dictionary.get('dog'))
print('cat' in my_dictionary)
print('monkey' in my_dictionary)

In your Notebook
----------------
Respond to the following:

Write down what was printed out. What type is my_dictionary? It is a class dict. It printed out entries in the disctionary sort of like a list but it's not ordered and doesn't use positions like [1] to get items.

Add a line of code that will print the definition of 'chair', then run the code again.

Write down what happens if you use my_dictionary['kittens']? What do you think that error means? There's an error. The error means there is no entry in the dictionary for 'kittens' so it can't fetch a definition
'''
my_dictionary = {
'cat': 'a domestic feline',
'dog': 'a domestic canine',
'chair': 'furniture piece for sitting',
'car': 'automobile',
'chair': 'furntiture piece for sitting',
}
print(my_dictionary['kittens'])