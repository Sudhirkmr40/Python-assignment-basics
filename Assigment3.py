##1. Why are functions advantageous to have in your programs?
# Functions reduce the need for duplicate code. This makes your programs shorter, easier to read, and easier to update 2.
#
##2. When does the code in a function run: when it's specified or when it's called?
#A fucntion is a block of code that runs only when it is called , function return a value using a return statement if one is specified a function can be called anywhere after the funcion has been declared by itself , a function does nothing
##3. What statement creates a function?
#def
##4. What is the difference between a function and a function call?
##using fucntion to do a particular task any poingt in program  is called as function call , a function is a procedure to achieve a calla
##5. How many global scopes are there in a Python program? How many local scopes?
##Python has two scopes for variables: Local scope: variables you create within a function are only available within the function. Global scope: variables you create outside of a function belong to the global scope and can be used everywhere.
##6. What happens to variables in a local scope when the function call returns?
#A local variable retains its value until the next time the function is called A local variable becomes undefined after the function call completes The local variable can be used outside the function any time after the function call completes
#
##7. What is the concept of a return value? Is it possible to have a return value in an expression?
#The specific value returned from a function is called the return value. When the return statement is executed, the function exits immediately, and the return value is copied from the function back to the caller. This process is called return by value.
##8. If a function does not have a return statement, what is the return value of a call to that function?
#As soon as the statement is executed, the flow of the program stops immediately and return the control from where it was called. The return statement may or may not return anything for a void function, but for a non-void function, a return value is must be returned. Take a step-up from those "Hello World" programs
##9. How do you make a function variable refer to the global variable?
#If you want to refer to a global variable in a function, you can use the global keyword to declare which variables are global.
##10. What is the data type of None?
#None is the special data type in Python. It just represents the absence of the value. In most of the languages which are available in the world, they consider None data type as NULL. Help your bottom line with top-quality talent.
#
##11. What does the sentence import areallyourpetsnamederic do?
#That import statement imports a module named areallyourpetsnamederic. (This isn’t a real Python module, by the way.) This function can be called with spam.bacon ().
##12. If you had a bacon() feature in a spam module, what would you call it after importing spam?
#If we have bacon () funtion in spam module then first we need to import the module and then we need to import the funtion too. from spam import bacon This above code is used to import funtions from given module. And then we can use the imported funtion for our own utilities.
#
##13. What can you do to save a programme from crashing if it encounters an error?
#Prevents program from crashing if an error occurs If an error occurs in a program, we don’t want the program to unexpectedly crash on the user. Instead, error handling can be used to notify the user of why the error occurred and gracefully exit the process that caused the error.
##14. What is the purpose of the try clause? What is the purpose of the except clause?
#What is the purpose of try ()? The try clause is the code between the try and except clauses. If there is no exception, only the try clause will be executed unless the clause is already complete. The try clause is bypassed if an exception occurs, and the except clause is executed instead.
#
#