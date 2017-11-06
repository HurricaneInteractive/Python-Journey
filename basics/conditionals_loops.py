

"""
If, Elif, Else
"""
check = "Hamburger"

# Checks the 'check' variable for each if or elif statement. If none return True, go to the else statement
if check == False:
    print("It is False")
elif check == "Hamburger":
    print("Yummm, Hamburgers")
elif check == 'Yo':
    print("Hello")
else:
    print("It is True")

"""
For Loop
"""
numbers = ["Nick", "Someone", "Bob"]

# Loops through list and prints out name (item)
for item in numbers:
    print("Hello", item)

"""
While Loops
"""
run = True
current = 1

# Loop will run as long as 'run' is equal to True
while run:
    if current == 100:
        run = False
    else:
        print(current)
        current += 1