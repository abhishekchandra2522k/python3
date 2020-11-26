from classes.game import Person, bcolors
from classes.magic import Spell

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

#Instantiation
player = Person(460, 65, 60, 34, ['fire', 'thunder', 'blizzard', 'meteor', 'cure','curate'])

enemy = Person(1200, 65, 45, 25, [])

running = True

i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print('=========================')
    player.choose_action()

    choice = input("Enter Action : ")
    index = int(choice) -1


    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "Points of damage.")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic: ")) - 1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + 'You don\'t have enough mp' + bcolors.ENDC)
            continue
            
        player.reduce_mp(spell.cost)

        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell.name + ' deals ' + str(magic_dmg) + " points of damage" + bcolors.ENDC)

    
    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()

    player.take_damage(enemy_dmg)

    print("Enemy attacks for", enemy_dmg)

    print('\n--------------------------------------------------\n')
    print("Enemy HP : ", bcolors.FAIL, str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()) + bcolors.ENDC + '\n')
    print("Player HP : ", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_maxhp()) + bcolors.ENDC + "\n")
    print("Your MP : ", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_maxmp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You WIN!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You LOSE!" + bcolors.ENDC)
        running = False
