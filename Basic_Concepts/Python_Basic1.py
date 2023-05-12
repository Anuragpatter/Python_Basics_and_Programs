# In python we have built in functions where we dont have to write too much of code like print function
print('Hello World')
print('Welcome')    # In order to print in another line 
print('My name is Anurag',21)   # Python gets the interger and string difference. It provides space b/w string and int on its own.

# VARIABLES IN PYTHON
# Variables save data in memory. We can get data back by referencing the variable.
name = 'Tim'          # 'Name' is the variable and 'Tim' is the value assigned to that variable.
print(name)

print('Tim is a boy')
print(name +' is a boy')     # Concatenation in python, variable 'Name' is concatenated to the string.
# Both print functions above give same output.
age = 19
# print(name +'is'+age)  // In python we can't concatenate string with integer. 
print(name+' is',age)    # Need to give space before string 
print(name,'is',age)     # Don't need to give space before string like told above.

# STRINGS -- Plain texts
print('Hi. \nHow are you')    # \n used for printing in another line without using print function.

# print('Hi. 'How are you')     //SHOWS ERROR
print('Hi.\'How are you')     # The quote after back slash will print.

print(name[0])    # To print the first letter of the string in variable 'name'.
print(name.upper())   # To convert strings to uppercase

a = 'ANU'
print(a.lower())     # To print in lowercase
print(a.islower())   # Check whether everything is lower 'a' has upper so output is False.
print(a.isupper())
print(a.lower().islower())     # output - TRUE    By joining functions
print(len(a))                # length of a string
print(name.index('i'))       # Position of a character in string or array.
print(name.replace('m', 'T'))     # replace function

#Numbers in python
print(34+23)
print(((23 + 34)/20)-42 )
num = 33           # num is of data type int
num2 = str(num)    # num2 will print 33 but the data type is string
print(num2)
print(type(num2))     # type() tell the data type
print('number is '+ num2)   # no error as type is str
print(abs(-4))    # absoulute value of integer so no negative sign.
print(max(4,5))   # Max value
print(min(4,6,45,7))   # Min value
print(round(2.45))     # round off value
print(bin(67))        # convert to binary string.

from math import *     # '*' means all, it has math functions
print(sqrt(100))
print(pow(3,6))

# USER INPUT
name = input('your name : ')
print (name)
age = input('your age : ')
print('Your name is ' + name + ' and age is '+ age)
print(type(age))    # here, age is input as a str not a int data type.
age2 = int(input('your age: '))    # Converted age to int data type from str
print(type(age2))

# 'Raise to power' in python is denoted by '**' 
print(2 ** 3 ** 2)
# Shows the right-left associativity of **
# Output: 512, Since 2**(3**2) = 2**9

# If 2 needs to be in power first, need to use parenthesis()
print((2 ** 3) ** 2)
# Output: 64