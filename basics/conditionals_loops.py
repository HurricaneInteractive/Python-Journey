

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


"""
Break & Continue
"""
playerhp = 260
enemydmg = 60

while playerhp > 0:
    playerhp -= enemydmg

    if playerhp <= 30
        playerhp = 30
    
    print("Enemy attacked player... Current Health:", playerhp)

    # As long as this statement is true
    if playerhp > 30:
        # It'll continue the loop and ignore eveything below it
        continue
    
    print("Health is low, flee successful")
    # since players health never goes below 0, we need to break out of the loop
    break