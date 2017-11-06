# Uncomment function calls to see the output


# Defines a new function
def new_func():
    print("This is a new function")

# new_func()

# Defines a function with 2 parameters
def function_with_arguements(str1, str2):
    print(str1)
    print(str2)

# function_with_arguements("This is arguement 1", "This is the second one")

# Defines a function with default arguements
def default_arguements(name = "a mystery", age = "unknown"):
    print("My name is", name, "and my age is", age)

# default_arguements()

# Defines a function with default arguements
def keyword_arguements(name = "a mystery", age = "unknown"):
    print("My name is", name, "and my age is", age)

# keyword_arguements(None, 27)
# keyword_arguements(age = 27, name = "Adro") # passes the agruements using a key, this can also be in a different order

# Defines a agruement with a infinite number of arguements - more flexible than infinite
# *people will convert all arguements into a list
def infinite_arguements(*people):
    for person in people:
        print("This person is", person)

# infinite_arguements("Adro", "Jimmy", "Nick", "Tim", "Luke", "King", "Amy")

# Defines a function which will return a value
def return_values(num1, num2):
    return num1 + num2

sum1 = return_values(5, 7)  # Assignment the return value of the function to the variable sum1
sum2 = return_values(11, 24)
print("First", sum1, "and second", sum2)
