# List in python 
# It is a list of different values of same or different data types fixed in a variable.
countries = ['United Kingdom', 'India', 'Ghana', 'Poland']   # list variable with 4 attributes.
print(countries)
print(countries[3])      # printing a single attribute using its index.
print(countries[2][0])   # print character of the attribute (index within index)
print(countries[1:])     # prints inclusively from index given to the end of list.
print(countries[1:3])    # Ranged as [inclusive : exclusive] index from list. So, index 1 is included and index 3 is not included.
print(countries[1:4])    # Now the last element is included as 4th index will be overflow index but won't be included so no error will be shown.

# print(countries[1:5])  ERROR shown as although 5 is excluded but there is no index 4 in the list.
print(type(countries))   # output will be -- list (bcz thats the type of variable)
countries[0] = 'China'   # Replacing attribute of some index from list.
print(countries)
print(countries[-1])     # Indexing from last attribute of list starts from -1.
print(countries[-3:-1])  # Same as before, [inclusive:exclusive] 
# But here in slicing the order for index should be straight bcz [from:to] means, [-1:-3] will give empty list.
print(len(countries))    # Total number of attributes in list.

li = ['India',34,True,56.7]   # Different data types can be used within a single list
print(li)
print(type(li))     # type for the whole li will be list
print(type(li[3]))    # type for a single attribute will be in accordance with its own data type.

# List can also be initialized by using the 'list()' constructor.
li2 = list(('Anurag', 'India', 56, False))
print(li2)

# LIST METHODS
list1 = [1,2,3,4,5]
list2 = ['banana', 'apples', 'mango', 'oranges']
list1.extend(list2)
print(list1)             # Concatenates list1 with list2

list2.append('cherry')   # append() is used only to add a new attribute at the end of a list.
print(list2)

list2.insert(2,'kiwi')   # insert() is used to add a new attribute at any index in a list.
print(list2)             # 'kiwi' is inserted at index 2 and other attributes shift.

list2.remove('apples')   # To delete a single element from the list by using the name of the element.
print(list2) 

list2.clear()    # Empty list means remove every elements from the list.
print(list2)

list2 = ['banana', 'apples', 'mango', 'oranges']    # To print the index number or location of an attribute in a list.
print(list2.index('mango'))                         # Syntax:- list_name.index('attribute_name') is used.

print(list2.count('apples'))      # Number of times an attribute has occured in a list.

list1 = [4,3,5,2,1] 
list1.sort()      # sort() function will print the list attributes in ascending order.
print(list1)

list1 = [4,3,5,2,1] 
list1.reverse()
print(list1)   # reverse() prints the list in reverse order from the last index to the first.

list3 = list2.copy()     # duplicate a list use copy() 
print(list3)                

list2 = ['banana', 'apples', 'mango', 'oranges']
list2.pop()      # To eliminate the last element of the list
print(list2)

list2 = ['banana', 'apples', 'mango', 'oranges']
print(list2.pop())    # Print the element to be popped from the list

list2 = ['banana', 'apples', 'mango', 'oranges']
list2.pop(1)      # Popping attribute with index number 1
print(list2)      # To delete attribute using index number and pop() function in the list

list2 = ['banana', 'apples', 'mango', 'oranges']
del list2[0]      # Using delete function to delete attribute at index 0 in the list.
print(list2)

del list2    # To delete entire list, means the list2 structure along with the attributes are deleted.

# print(list2)    {For del function, list Structure also eliminated that's why error will be shown}
# In clear() function, the list's attributes/elements are deleted but empty structure of the list remains.


# TUPLES IN PYTHON:
# Used to store multiple items in a single variable (different from list)
# Tuples are IMMUTABLE: Values can't be changed.
num = (1,2,3)      # Syntax for tuple
print(num)
print(type(num))   # Data_type/class : 'Tuple' for whole variable 'num'
print(num[0])      # Print element of index 0 of the tuple

# num[1] = 23 Changing value of an attribute 
# Shows TypeError because tuples are immutable  

num1 = (1,2,3,1,'land',True)     # Allows repetition of attribute values & multiple data_types
print(num1)
print(type(num1[2]))    # data_type of element on tuple index 2
num2 = tuple((1, 'home', True, 23, 3.4))    # Initializing by tuple consrtructor


# FUNCTIONS IN PYTHON: Block of code that performs a particular task, allows to restructor code well.
def greet_function():    # Syntax: def function_name():        // Here, 'def' is keyword used to define functions.
    print('Welcome User')    # Task of function is to PRINT, if print() has no indentation then its invalid syntax.

# Indentation tells what's included in the function, 1 indentation = 4 spaces
# We "call the funtion" when we need to execute the task, such as:- 
greet_function()    # Calling the function

def greeting_function(name):     # Passing an Argument/Parameter (name) in the function
    print('Welcome '+name)
greeting_function('John')    # Passing value to the argument(name) when calling the function

# Argument is just like a Variable (just specifically for the funtion it was passed in)
# So when the function is called argument can be given different values.
greeting_function('Amy')    # Data_type of argument value is string

# greeting_function(34)  Shows Error bcz default data_type is string
greeting_function(str(34))    # Calling function
# OR change it in the function task itself
def greetings_function(name):
    print('Welcome '+ str(name))
greetings_function(32)

def greet_func(name,age):     # Passing multiple arguments
    print('Welcome '+name+' Your age is '+str(age))   # age is integer
greet_func('John',34)
# Same as above one, another method to pass values useful when taking input form user.
greet_func(name= 'John', age = 23)     # To pass same or other variables as values of agruments

def greet(*names):        # '*' when number and data_type of values to argument is unknown
    print('Welcome '+names[1])    # Index number 1 is used to greet 'Tim'
greet('John','Tim','Ron')

# Program using function and user input:-
def greet_function(name,age):      # Arguments passed are: name,age
    print('Welcome '+name+' Your age is '+str(age))

a = input('Enter your name: ')    # Other variable for 'name' is a
b = input('Enter your age: ')     # Other variable for 'age' is b
greet_function(a,b)       # New variables used as values of arguments while calling function