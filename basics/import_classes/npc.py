# Create a new Class called Enemy
class NPC:
    # init function that runs when object is created
    def __init__(self, hp):
        self.max_hp = hp
        self.hp = hp
    
    def getHp(self):
        print("NPC Hp is", self.hp)