# imports the regular expression library
import re

# prints out a welcome message
print("Our Magical Calculator")
print("Type 'quit' to exit\n")

# global functions
previous = 0
run = True

# Defines the main program function
def perform_math():
    # get the global functions, they won't be available due to function scope
    global run
    global previous
    equation = ""
    
    # if there hasn't been a previous equation
    if previous == 0:
        # ask the user for a input
        equation = input("Enter equation:")
    else:
        # otherwise, start with the previous value
        equation = input(str(previous))

    # if the person enters 'quit'
    if equation == 'quit':
        # set run to False which will close the program
        print("Goodbye, human")
        run = False
    # otherwise calculate math
    else:
        # uses regular expression to get rid of dangerous charaters in user input
        equation = re.sub('[a-zA-z,.:()" "]', '', equation)

        # if there hasn't been a previous equation
        if previous == 0:
            # evaluate the result
            previous = eval(equation)
        # Otherwise
        else:
            # evaluate result of the previous result and new equation
            previous = eval(str(previous) + equation)

# While the application is running, call the perform_math function
while run:
    perform_math()