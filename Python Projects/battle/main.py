import random

# importing game.py, magic.py, inventory.py
from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

# Create Black Magic (DAMAGE)
# class Spell=> (name, cost, dmg, type)
fire = Spell("Fire", 20, 600, 'black')
thunder = Spell("Thunder", 24, 720, 'black')
blizzard = Spell("Blizzard", 20, 580, 'black')
meteor = Spell("Meteor", 40, 1600, 'black')
quake = Spell("Quake", 28, 840, 'black')

# Create White Magic (CURE)
# class Spell => (name, cost, dmg, type)
cure = Spell("Cure", 24, 720, "white")
cura = Spell("Cura", 28, 840, "white")
curea = Spell("Curea", 36, 1080, "white")
curate = Spell("Curate", 40, 1200, "white")

# Create Some Items (DAMAGE + CURE both options available)
# class Item => (name, type, description, prop)
potion = Item("Potion", "potion", "Heals 150 HP", 150)
hipotion = Item("Hi-potion", "potion", "Heals 300 HP", 300)
superpotion = Item("Super-potion", "potion","Heals 1000 HP", 1000)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one player", 9999)
hielixer = Item("Mega-Elixer", "elixer", "Fully restores HP/MP of all members", 9999)
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

# player defining
player_magic = [fire, thunder, blizzard, meteor, cure, curate]

player_items = [{'item' : potion,'quantity' : 15}, 
                {'item' : hipotion, 'quantity' : 5}, 
                {'item' : superpotion, 'quantity' : 5}, 
                {'item' : elixer, 'quantity' : 5},
                {'item' : hielixer, 'quantity' : 2}, 
                {'item' : grenade, 'quantity' : 5}]

enemy_spells = [fire, meteor, curate]

#Instantiation of players and enemy
# class Person => (name, hit_point, magic_point, attack, defence, magic_choice, item_choice)
player1 = Person("Valos",3000, 132, 160, 100, player_magic, player_items)
player2 = Person("Nick ",3560, 188, 180, 120, player_magic, player_items)
player3 = Person("Robot",4460, 174, 260, 140, player_magic, player_items)

players = [player1, player2, player3]

enemy1 = Person("Imp  ", 1200, 130, 300, 325, enemy_spells, [])
enemy2 = Person("Magus",20000, 240, 480, 225, enemy_spells, [])
enemy3 = Person("Imp2 ", 1200, 130, 300, 325, enemy_spells, [])

enemies = [enemy1, enemy2, enemy3]

running = True

i = 0

# Start Game
print(bcolors.FAIL + bcolors.BOLD + "\n\nAN ENEMY ATTACKS!" + bcolors.ENDC)

# Options for User
while running:
    print('------------------------------------------------------------\n\n')
    print(bcolors.BOLD + "PLAYER NAME   HP                                  MP" + bcolors.ENDC)
    
    #print player stats
    for player in players:
        player.get_stats()

    #print enemy stats
    for enemy in enemies:
        enemy.get_enemy_stats()

    print("\n")

    for player in players:
       
       # Player can choose action 1. Attack 2. Magic 3. Items
        player.choose_action()      

        choice = input("\tChoose Action : ") 

        index = int(choice) -1

        # ATTACK chosen, player attacked for a random value between atkl, atkh
        if index == 0:  
            dmg = player.generate_damage() 
            
            # choose target
            enemy = player.choose_target(enemies)

            enemies[enemy].take_damage(dmg)
            
            print("\n" + bcolors.OKGREEN + player.name.replace(" ", ""),"attacked " + bcolors.ENDC + 
                bcolors.FAIL + enemies[enemy].name.replace(" ", "") + bcolors.ENDC + bcolors.OKGREEN + " for", dmg, "Points of damage." + bcolors.ENDC)

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ", "") + " has died.")
                del enemies[enemy]

        # MAGIC choosen, choose magic from options 
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("\tChoose magic: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + 'You don\'t have enough mp' + bcolors.ENDC)
                continue
                
            player.reduce_mp(spell.cost)
            
            # white magic
            if spell.type == "white": 
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for " + str(magic_dmg) + "HP."+ bcolors.ENDC)
            
            # black magic
            elif spell.type == "black":
                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + ' deals ' + str(magic_dmg) + " points of damage to "+ bcolors.ENDC 
                    + bcolors.FAIL + enemies[enemy].name.replace(" ", "") + bcolors.ENDC)
                
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ","") + " has died.")
                    del enemies[enemy]

        # ITEM chosen, choose from item options
        elif index == 2:
            player.choose_items()
            item_choice = int(input("\tChoose item: ")) - 1

            if item_choice == -1:
                continue
            
            item = player.items[item_choice]["item"]
            player.items[item_choice]['quantity'] -= 1

            if player.items[item_choice]['quantity'] < 0:
                print(bcolors.FAIL +  "\n" +  "None left..." + bcolors.ENDC)
                continue

            if item.type == 'potion':
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for " + str(item.prop) + " HP." + bcolors.ENDC)
            
            elif item.type == 'elixer':

                if item.name == "Mega-Elixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                
                print(bcolors.OKGREEN + "\n" + item.name + " fully restores player's HP/MP" + bcolors.ENDC)

            elif item.type == 'attack':
                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " deals " + str(item.prop) + " damage to " 
                    + bcolors.ENDC + bcolors.FAIL + enemies[enemy].name.replace(" ", "") + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has died.")
                    del enemies[enemy]

    # 3-3 player-enemy gameplay, Check if battle is over
    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1  
    
    #check if player won
    if defeated_enemies == 2:
        print(bcolors.OKGREEN + bcolors.BOLD + "\nYou WIN!" + bcolors.ENDC)
        running = False

    #check if player lose
    if defeated_players == 2:
        print(bcolors.FAIL + bcolors.BOLD + "\nYou LOSE!" + bcolors.ENDC)
        running = False  

    print("\n -----------------------------------------------------------------")
    # enemy configuration (attack phase)

    for enemy in enemies:
        enemy_choice = random.randrange(0,2)

        if enemy_choice == 0:
            # chose attack
            target = random.randrange(0,3)
            enemy_dmg = enemy.generate_damage()

            players[target].take_damage(enemy_dmg)
            print("\n")
            print(bcolors.BOLD + bcolors.FAIL + enemy.name.replace(" ","") +" attacks " + bcolors.ENDC 
            + bcolors.OKGREEN + players[target].name.replace(" ", "") + bcolors.ENDC 
            + bcolors.FAIL + bcolors.BOLD + " for " + str(enemy_dmg) + " Points of damage." + bcolors.ENDC)
        
        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)
            
            # white magic
            if spell.type == "white": 
                enemy.heal(magic_dmg)
                print(bcolors.FAIL + bcolors.BOLD + spell.name + " heals "+ enemy.name +" for " + str(magic_dmg) + "HP."+ bcolors.ENDC)
            
            # black magic
            elif spell.type == "black":
                target = random.randrange(0,3)

                players[target].take_damage(magic_dmg)
                print(bcolors.FAIL + "\n" + bcolors.BOLD + enemy.name.replace(" ","") + "'s " + spell.name + ' deals ' + str(magic_dmg) + " points of damage to "+ bcolors.ENDC 
                    + bcolors.OKGREEN + players[target].name.replace(" ", "") + bcolors.ENDC)
                
                if players[target].get_hp() == 0:
                    print(players[target].name.replace(" ","") + " has died.")
                    del players[target]

            #print(enemy.name.replace(" ","") + " chose", spell.name, "damage is", magic_dmg)
