# Importing a class using relative paths
from import_classes.npc import NPC


# Create a new Class called Enemy
class Enemy:
    # "static" variable, can't be changed when object is created
    hp = 200
    # init function that runs when object is created
    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    # define and function and passing in self (reference to object)
    def getAtk(self):
        # need to use self to get variable values
        print("Atk is", self.atkl)
    
    def getHp(self):
        print("Hp is", self.hp)


enemy1 = Enemy(40, 49)
enemy1.getAtk()
enemy1.getHp()

enemy2 = Enemy(75, 90)
enemy2.getAtk()
enemy2.getHp()

# Using class defined in the import_classes folder.
# Recommended to move classes into a separate folder
npc = NPC(150)
npc.getHp()