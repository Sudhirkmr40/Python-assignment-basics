#1. What does an empty dictionary's code look like?
#just two curly braces, like this: {}
#2. What is the value of a dictionary value with the key 'foo' and the value 42?
#valur
#Dictionary = {foo:42}
#
#3. What is the most significant distinction between a dictionary and a list?
#dictionary is orderd collections of elements with key value pairs and is enclosed by curly brackets
#while list  are used to store multiple items in a single variable. and is enclosed by square brackets.
#
#
#4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
#ans - program will be failed as value for key 'foo' is not found
#
#
#5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
#spam = {'cat':30}
#print(spam)
#l=spam.keys()
#print(l)
#{'cat': 30}
#dict_keys(['cat'])
#
#6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
#
#spam = {'cat':30}
#print(spam)
#l=spam.values()
#print(l)
#dict_values([30])
#
#7. What is a shortcut for the following code?
#
#if 'color' not in spam:
#spam['color'] = 'black'
#7. What is a shortcut for the following code?
#if 'color' not in spam: spam['color'] = 'black'
#
#spam.setdefault('color', 'black')
#
#8. How do you "pretty print" dictionary values using which module and function?
#pprint.pprint()

