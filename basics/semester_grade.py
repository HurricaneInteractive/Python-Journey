"""
Challenge
Calculate the overall mark of a student give their percentage of a assessment item & assessment weighting to the overall mark for that unit
eg: 88 (student mark), 15 (weighting)
This is version was created on the 6/11/17 based on the calculator.py project
Updates to this program will be listed below
"""
# Import regex package
import re

# Inital program state
run = True

# Welcome message
print("Welcome to the grade calculator")
print("Type 'quit' to close program\n")

# Returns the Grade Scale based on overall_mark
def get_grade_scale(grade):
    # converts into float type
    grade = float(grade)
    # if else statement to get the correct grade scale
    if grade >= 85:
        return 'HD'
    elif grade >= 74:
        return 'D'
    elif grade >= 65:
        return 'C'
    elif grade >= 50:
        return 'P'
    else:
        return 'I have some bad news...'

def calculate_overall_mark():
    # Global program state
    global run
    # Gets the users input
    grades = input("Input grade and weight groups as follows 88:15,66:20\n")
    # resets/sets the overall mark variable
    overall_mark = 0

    # if the user enters 'quit'
    if grades == "quit":
        # close program + thank you message
        print("Thank you for your time")
        run = False
    # Otherwise continue
    else:
        # Removes everything that isn't a number or the symbols : ,
        grades = re.sub('[^0-9:,]', '', grades)
        # Splits into grouping ['85:15', '66:20']
        grade_grouping = grades.split(',')
        # Loops through grouping
        for group in grade_grouping:
            # Splits into separate values ['85', '15']
            marks = group.split(':')
            # Calculates the overall mark, need to convert into int
            overall_mark += (int(marks[0])/100) * int(marks[1])
        # rounds float to 2 decimal points
        rounded = "%.2f" % overall_mark
        
        # Prints out the overall rounded grade
        print("Overall mark:", rounded)
        # Prints out return value of grade scale function
        print("Grade Scale:", get_grade_scale(rounded), '\n')

# Checks if program is running
while run:
    # Run calculate function
    calculate_overall_mark()

"""
Known problems / bugs:
- It is possible for the input to end up being '':''
- Total weighting may not equal 100%
- No check to see if grade is over 100%
"""