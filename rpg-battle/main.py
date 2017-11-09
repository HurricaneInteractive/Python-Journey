'''
    RPG TEXT BASED BATTLE
    This is a cool idea however there is a LOT of repetitive code that can be cleaned up

    INTERESTING IDEAS
    Use JSON to save player information
    Use JSON as a enemy db and randomly select some during battle
'''

import random
from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

# Create Black magic
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 32, 1500, "white")


# Create items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 1000 HP", 1000)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("Mega Elixer", "elixer", "Fully restores HP/MP of all party members", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_magic = [fire, thunder, blizzard, meteor, cure, cura]
enemy_spells = [fire, meteor, cure]

player_items = [
    {"item": potion, "quantity": 15}, 
    {"item": hipotion, "quantity": 5},  
    {"item": superpotion, "quantity": 5},  
    {"item": elixer, "quantity": 3},  
    {"item": hielixer, "quantity": 1},  
    {"item": grenade, "quantity": 1}
]

# Instantiate People
player1 = Person("Valos:", 3260, 132, 300, 34, player_magic, player_items)
player2 = Person("Nick :", 4160, 188, 311, 34, player_magic, player_items)
player3 = Person("Robot:", 3089, 174, 288, 34, player_magic, player_items)

enemy1 = Person("Imp  ", 1200, 120, 300, 325, enemy_spells, [])
enemy2 = Person("Magus", 10000, 221, 350, 25, enemy_spells, [])
enemy3 = Person("Imp  ", 1200, 120, 300, 325, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("=================")

    # Prints Stats
    print("\n")
    print("NAME                HP                                  MP")
    for player in players:
        player.get_stats()
    
    print("\n")
    
    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        choice = input("Choose action: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print("You attacked " + enemies[enemy].name.replace(" ", "") + " from", dmg, "points of damage.")

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ", "") + " has been defeated")
                del enemies[enemy]

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose Magic: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "points of HP" + bcolors.ENDC)
            elif spell.type == "black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)

                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has been defeated")
                    del enemies[enemy]

        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose Item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]
            item_quantity = player.items[item_choice]["quantity"]
            
            if item_quantity == 0:
                print(bcolors.FAIL + '\n' + "None left..." + bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)
            elif item.type == "elixer":
                if item.name == "Mega Elixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                
                print(bcolors.OKGREEN + "\n" + item.name + " fully restored HP/MP" + bcolors.ENDC)
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)

                print(bcolors.FAIL + "\n" + item.name + " dealt", str(item.prop), "of damage." + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has been defeated")
                    del enemies[enemy]

    # Check if battle is over
    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1
    
    if defeated_enemies == len(enemies) - 1:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif defeated_players == len(players) - 1:
        print(bcolors.FAIL + "You lost :(" + bcolors.ENDC)
        running = False

    # Enemy Attack phase
    for enemy in enemies:
        enemy_choice = random.randrange(0, 3)

        # Chose attack
        if enemy_choice == 0:
            target = random.randrange(0, 3)
            enemy_damage = enemy.generate_damage()

            players[target].take_damage(enemy_damage)
            print(enemy.name.replace(" ", "") + " attacks " + players[target].name.replace(" ", "") + " for", str(enemy_damage) + ".")
        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)
            
            if spell.type == "white":
                enemy.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals " + enemy.name + " for", str(magic_dmg), "points of HP" + bcolors.ENDC)
            elif spell.type == "black":
                target = random.randrange(0, 3)
                players[target].take_damage(magic_dmg)

                print(bcolors.OKBLUE + "\n" + enemy.name.replace(" ", "") + "'s " + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

                if players[target].get_hp() == 0:
                    print(players[target].name.replace(" ", "") + " has been defeated")
                    del players[target]
