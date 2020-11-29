# importing game.py, magic.py, inventory.py
from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

# Create Black Magic
fire = Spell("Fire", 10, 100, 'black')
thunder = Spell("Thunder", 12, 124, 'black')
blizzard = Spell("Blizzard", 10, 100, 'black')
meteor = Spell("Meteor", 20, 200, 'black')
quake = Spell("Quake", 14, 140, 'black')

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 14, 180, "white")
curea = Spell("Curea", 18, 200, "white")
curate = Spell("Curate", 20, 220, "white")

# Create Some Items
# (name, type, description, prop)
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super-potion", "potion","Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one player", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores HP/MP of all members", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)


#Instantiation of player and enemy

player_magic = [fire, thunder, blizzard, meteor, cure, curate]
player_items = [potion, hipotion, superpotion, elixer, hielixer, grenade]

player = Person(460, 65, 60, 34, player_magic, player_items)

# Person class -> (hit_point, magic_point, attack_high, attack_low, magic_choice)

enemy = Person(1200, 65, 45, 25, [],[])

running = True

i = 0

# Start Game
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

# Options for User
while running:
    print('=========================')
    player.choose_action()      # Player can choose action 1. Attack 2. Magic

    choice = input("Choose Action : ") 
    index = int(choice) -1

    # ATTACK chosen, player attacked for a random value between atkl, atkh
    if index == 0:  
        dmg = player.generate_damage() 
        
        enemy.take_damage(dmg)
        
        print("You attacked for", dmg, "Points of damage.")
    
     # MAGIC choosen, choose magic from options 
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic: ")) - 1

        if magic_choice == -1:
            continue

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + 'You don\'t have enough mp' + bcolors.ENDC)
            continue
            
        player.reduce_mp(spell.cost)

        if spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals for " + str(magic_dmg) + "HP."+ bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + ' deals ' + str(magic_dmg) + " points of damage" + bcolors.ENDC)

    # ITEM chosen, choose from item options
    elif index == 2:
        player.choose_items()
        item_choice = int(input("Chooe item: ")) - 1

        if item_choice == -1:
            continue
        
        item = player.items[item_choice]

        if item.type == 'potion':
            player.heal(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name + " heals for " + str(item.prop) + " HP." + bcolors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()

    player.take_damage(enemy_dmg)

    print("Enemy attacks for", enemy_dmg)

    print('--------------------------------------------------')

    print("Enemy HP : ", bcolors.FAIL, str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()) + bcolors.ENDC + '\n')
    print("Player HP : ", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_maxhp()) + bcolors.ENDC + "\n")
    print("Your MP : ", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_maxmp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You WIN!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You LOSE!" + bcolors.ENDC)
        running = False
