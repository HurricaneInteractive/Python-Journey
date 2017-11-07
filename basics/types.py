# Copy each line into the python3 console to see the output

"""
Numbers
"""
5       # int
5.43    # float
5 + 5   # Mathematical operation of a number
5.5 + 5.5   # This will return 11.0 because the operation was done on a float
"5" + "5"   # Will return "55", this is concatenating two string
int("5")    # This will covert the string "5" into a number
int("5") + int("5")     # returns 10
# int("Hello")    # NOT valid as "Hello" cannot be used as a number

"""
Strings
"""
"Hello World"   # Characters wrapped in double quotes
'Hello World'   # Characters wrapped in single quotes
# 'Don't do that  # This will return an error because the quote is ending before the sentence is done
'Don\'t do that'    # Use a backslash to 'escape' the single quote
print('She said "Don\'t do that"')  # Using both single & double quotes + escaping a single quote in the middle

"""
String Manipulation
"""
"Hello, " + "Adro"  # Concatenating two strings
# "The costs " + 6 + " bucks" # Error can't concat a string and integer
"This costs " + str(6) + " dollars"  # Converts 6 into a string
"This costs " + str(6 + 5) + " dollars"  # Can to math inside of the str()
"Hello:Adro".split(":") # Creates the list of split values ['Hello', 'Adro']
"My name is " + "Hello:Adro:World".split(":")[1]    # Gets my name in the split list and then concatenates the string

"""
Booleans
- Checks the value and type
"""
True
False
5 == 5  # True
5 == 4  # False
5 is 5  # True
5 is not 5  # False
"This" is "This"    # True
"This" is "this"    # False
"True" is True  # False, one is string the other is a boolean
"True" is str(True) # True

"""
Lists (aka Arrays)
"""
["Movies", "Games", "Python"]   # Define a list - Index starts at 0
["Movies", "Games", "Python"][0]    # "Movies"
print("I Like " + ["Movies", "Games"][1]) # Prints out I Like Games
print(["Movies", 6, "Something"][1])    # Can't convert int to string
["Movies", "Games"].append("Python")    # Adds value to list

"""
Dictionaries (aka JavaScript Objects (key + value pair))
"""
{"name": "Adro", "age": 20, "hobby": "Code"}    # Defines a dictonary
{"name": "Adro", "age": 20, "hobby": "Code"}['name']    # Gets the name value using the key

"""
Variables
"""
greeting = "Hello World"    # Defines a variable called greeting
print(greeting) # This will return "Hello World"
greeting = greeting.split(" ")[0]   # Sets greeting to the first item in the split list (Hello)
print(greeting) # Returns Hello
print(greeting + " Adro")   # Concats name after greeting
greeting = greeting + " Adro"   # New value: Hello Adro

number = 1
second = 2
print(number * second + second * number)    # aka print(1 * 2 + 2 * 1)

check = True

