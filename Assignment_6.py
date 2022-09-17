1. What are escape characters, and how do you use them?
In Python strings, the backslash "\" is a special character, also called the "escape" character. It is used in representing certain whitespace characters: "\t" is a tab, "\n" is a newline, and "\r" is a carriage return.
2. What do the escape characters n and t stand for?
n = new line
t = new tab
3. What is the way to include backslash characters in a string?
The \ escape character will represent a backslash character.
4. The string "Howl's Moving Castle" is a correct value. Why isn't the single quote character in the word Howl's not escaped a problem?
double quotes are used to quotes mark the beginning and end of the string

5. How do you write a string of newlines if you don't want to use the n character?

#Multiline strings allow you to use newlines in strings without the \n escape character.
#6. What are the values of the given expressions?
#s='Hello, world!'[1]
#s='Hello, world!'[0:5]
#s='Hello, world!'[:5]
#s='Hello, world!'[3:]
#
#e
#Hello
#Hello
#lo, world!
#
#7. What are the values of the following expressions?
#
#'Hello'.upper()
#'Hello'.upper().isupper()
#'Hello'.upper().lower()
#
#HELLO
#True
#hello
#
#
#
#8. What are the values of the following expressions?
#
#s1='Remember, remember, the fifth of July.'.split()
#s2='-'.join('There can only one.'.split())
#
#['Remember,', 'remember,', 'the', 'fifth', 'of', 'July.']
#There-can-only-one.
#
#9. What are the methods for right-justifying, left-justifying, and centering a string?
#The rjust(), ljust(), and center() string methods, respectively
#
#10. What is the best way to remove whitespace characters from the start or end?
#The lstrip() and rstrip() methods remove whitespace from the left and right ends of a string, respectively.
#