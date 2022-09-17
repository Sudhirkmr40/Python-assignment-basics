#1. What exactly is []?
# he empty list value, which is a list value that contains no items. This is similar to how '' is the empty string value.
#2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam

spam = [2,4,6,8,10]
print(spam)
spam.insert(3,"hello")
print(spam)

#Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.

spam = ['a', 'b', 'c', 'd']
print(spam)
x =spam[-1]
print(x)
y = spam[:2]
print(y)

z = spam[int(int('3' * 2) / 11)]
print(z)
#3. What is the value of spam[int(int('3' * 2) / 11)]? "d"
#4. What is the value of spam[-1]?"d"
#5. What is the value of spam[:2]? a,b

#Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True] for the next three questions.
bacon = [3.14, 'cat', 11, 'cat', True]
print(bacon)
x=bacon.index('cat')
print(x)
y = bacon.append(99)
print(y)

z = bacon.remove('cat')
print(z)

#6. What is the value of bacon.index('cat')?1
#7. How does bacon.append(99) change the look of the list value in bacon? [3.14, 'cat', 11, 'cat', True, 99]
#8. How does bacon.remove('cat') change the look of the list in bacon? [3.14, 11, 'cat', True, 99]

#9. What are the list concatenation and list replication operators?
#The operator for list concatenation is +, while the operator for replication is *.

#10. What is difference between the list methods append() and insert()?


#While append() will add values only to the end of a list, insert() can add them anywhere in the list.
#11. What are the two methods for removing items from a list?

#The del statement and the remove() list method are two ways to remove values from a list.
#12. Describe how list values and string values are identical.

#13. What's the difference between tuples and lists?
#14. How do you type a tuple value that only contains the integer 42?
(42,)
(42,)
#15. H
#15. How do you get a list value's tuple form? How do you get a tuple value's list form?
#The tuple() and list() functions, respectively
#16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?
#They contain references to list values.
#17. How do you distinguish between copy.copy() and copy.deepcopy()?

#he copy.copy() function will do a shallow copy of a list, while the copy.deepcopy() function will do a deep copy of a list. That is, only copy.deepcopy() will duplicate any lists inside the list.

