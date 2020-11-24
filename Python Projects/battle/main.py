from classes.game import Person, bcolors

magic = [{'Name' : 'Fire', 'cost' : 10, 'dmg' : 60},
         {'Name' : 'Thunder', 'cost' : 12, 'dmg' : 80},
         {'Name' : 'Bllizard', 'cost' : 10, 'dmg' : 60}]

player = Person(460, 65, 60, 34, magic)

enemy = Person(1200, 65, 45, 25, magic)

running = True

i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print('=========================')
    player.choose_magic()

    choice = input("Enter Action : ")
    index = int(choice) -1

    print('You chose', player.generate_spell_name(int(index)))

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "Points of damage. Enemy HP ", enemy.get_hp())
 