#1.What are the two values of the Boolean data type? How do you write them?
# True and false
# True is written as boolA and False is written as bool B

#2. What are the three different types of Boolean operators?
# there 3 types of boolen operators AND,OR,NOT

#3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).

#4. What are the values of the following expressions?
#(5 > 4) and (3 == 5)   = False
#not (5 > 4) - Fale
#(5 > 4) or (3 == 5)  True
#not ((5 > 4) or (3 == 5)) False
#(True and True) and (True == False) = False
#(not False) or (not True)  = True


#5. What are the six comparison operators?
#==  ( Equal)
#!=  ( Not equal)
#>  (Greater than)
##<  (Less than)
#>=  (Greater than or equal to)
#<= (Less than or equal to)

#6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
#assignment operator is used to assign value to a variable
#Equal to Operator "=="
#It is a relational or comparison operator

#7. Identify the three blocks in this code:

spam = 0  # 1st block
if spam == 10: # second block
    print('eggs')
if spam > 5: # 3rd block
    print('bacon')
else:
    print('ham')
    print('spam')
    print('spam')

#8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
a = "spam"
if a == int(1):
    print("Hello")
elif a == int(2):
    print("Howdy")
else:
    print("greetings")
#9.If your programme is stuck in an endless loop, what keys you’ll press?
#if programme stuck in a endless loop , the we can restart interpreter or cntrl+c to exit from loop

#10. how can you tell the difference in break and continue?
#break statement is used to break or exit from for or while loop conditional loops when the loop ends the code picks
#up from and exeutes the next line immediately

#Ans - No
#n##ot diffrence


#12. Write a short program that prints the numbers 1 to 10 using a for loop.
 #   Then write an equivalent program that prints the numbers 1 to 10 using a while loop




#11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

for i in range(10):
    print(i)

for j in range(0,10):
    print(j)

for k in range(0,10,1):
    print(k)

l = []
for l in range (10):
    print(l)

m = 1
while m <10:
    print(m)
    m += 1

i = 1
while i < 6:
  print(i)
  i += 1
#. If you had a function named bacon() inside a module named spam, how would you call it after importing spam

#ans = spam.bacom()





