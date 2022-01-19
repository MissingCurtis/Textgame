"""" Jon Curtis """


# Function showing the goal of the game and move commands
def show_instructions():
    # print a main menu and the commands
    print("The Argos Text Adventure Game")
    print("Collect  all 6 items to win the game, or be eaten by the Monster.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")
    print('To Exit the game type "exit".')


# Functions
def space_suit():
    if 'Space Suit' in inventory:
        print('The Space Monster lunges towards you slamming you across the room!')
        print('Your Space suit absorbs most of the damage.')

    else:
        print('The Space Monster lunges towards you slamming you across the room!')
        print('You had nothing to protect you from the damage!')
        print('Luckily you are passed out when the monster starts to consumes you!')
        print('Game over')


def oxygen_tank():
    if 'Oxygen tank' in inventory:
        print('You take a deep breath and get to your feet.')
        print('The Space Monster seems to be emitting some type of fumes.')
    else:
        print('You take a deep breath and the world spins!')
        print('The Space Monster must produce toxic fumes!')
        print('Luckily you are passed out when the monster consumes you!')
        print('Game over')


def electric_baton():
    if 'Electric baton' in inventory:
        print('You swing wildly at the Monster backing it into the open core!')
        print('The Space Monster seems to be effected by the electric shocks.')
    else:
        print('You hit the Monster with a chair!')
        print('The Monster is unaffected, you needed something more powerful!')
        print('You are awake when the monster starts to consume you!')
        print('Game over')


def core_key():
    if 'Fusion core key' in inventory:
        print('You slam the core shut!')
        print('The Fusion core key locks the core closed!')
    else:
        print('You slam the core shut!')
        print('You can not lock the core and the Monster bashes the door open!')
        print('You are awake when the monster consumes you!')
        print('Game over')


def engine_code():
    if 'Engine initiation code' in inventory:
        print('You turn on the console to activate the engines!')
        print('The Space Monster is trying to break the core door open, as you punch in the Engine initiation code!')
    else:
        print('You turn on the console to activate the engines!')
        print('The Space Monster is trying to break the core door open, you do not have the code to start the engines!')
        print('The Monster breaks the core open, you are awake when the monster consumes you!')
        print('Game over')


def safety_chip():
    if 'Safety override' in inventory:
        print('The console flashes a warning about foreign objects in the core!')
        print('You insert the Safety override and start the engine!')
        print('You breath a sigh of relief as the Space Monster is torn apart at a molecular level.')
        print('Congratulations you have won!')
    else:
        print('The console flashes a warning about foreign objects in the core!')
        print('The engine initiation shuts down without a Safety override, the Monster breaks out of the core!')
        print('You are awake when the monster starts to consume you!')
        print('Game over')


# The dictionary links a room to other rooms.
rooms = {
        'Mess deck': {'name': 'Mess deck', 'South': 'Armory', 'North': 'Repair locker',
                      'West': 'Bridge', 'East': 'Cargo', 'exit': 'exit',
                      'text': 'The lights flicker on and off. You seem to be alone.',
                      'exits': 'There are exits to the North, South, East, and West.',
                      'contents': []},
        'Bridge': {'name': 'Bridge', 'East': 'Mess deck', 'exit': 'exit',
                   'text': 'The Bridge is too silent, several consoles are smashed.',
                   'exits': 'There is an exit to the East.',
                   'contents': ['Safety override']},
        'Armory': {'name': 'Armory', 'North': 'Mess deck', 'East': 'Airlock',
                   'exit': 'exit',
                   'text': 'It looks like its been emptied.',
                   'exits': 'There are exits to the North and East.',
                   'contents': ['Electric baton']},
        'Crew Berthing': {'name': 'Crew Berthing', 'West': 'Repair locker', 'exit': 'exit',
                          'text': 'Its dark in here and the floors are sticky',
                          'exits': 'There is an exit to the West.',
                          'contents': ['Fusion core key']},
        'Airlock': {'name': 'Airlock', 'West': 'Armory', 'exit': 'exit',
                            'text': 'Looks like the outer door is damaged.',
                            'exits': 'There is an exit to the West.',
                            'contents': ['Space Suit']},
        'Cargo': {'name': 'Cargo', 'West': 'Mess deck', 'North': 'Engineering', 'exit': 'exit',
                          'text': 'Smashed cargo lays around you.',
                          'exits': 'There are exits to the North and West.',
                          'contents': ['Engine initiation code']},
        'Engineering': {'name': 'Engineering',
                        'text': 'A monster stands before you!',
                        'exits': 'There is no escape!',
                        'contents': []},
        'Repair locker': {'name': 'Repair locker', 'East': 'Crew Berthing', 'South': 'Mess deck',
                          'exit': 'exit',
                          'text': 'Chunks of something lay on the ground, you try not to think about it.',
                          'exits': 'There are exits to the South and East',
                          'contents': ['Oxygen tank']},
        'exit': {'name': 'Exit', 'text': 'Would you like to leave? "yes" or "no"',
                 'exits': 'You do not see a way out.', 'contents': []}
}

command_list = ['go', 'yes', 'no', 'exit', 'get']
directions = ['North', 'South', 'East', 'West']
current_room = rooms['Mess deck']
inventory = []
show_instructions()
# game loop
while True:
    # display current location
    if current_room is not rooms['Engineering']:
        print()
        print('You are in the {}.'.format(current_room['name']))
        print(current_room['text'])
        print(current_room['exits'])
    # display items
    if current_room['contents'] and len(current_room['contents']) > 0:
        print('You see a {}.'.format(', '.join(current_room['contents'])))
    # get user input
    command = input('What do you do? ').strip()
    # bad command
    if command == '':
        print('Invalid command')
        command = input('What do you do? ').strip()
    if command.split()[0] not in command_list:
        print("Invalid command")
    # movement
    if command.split()[0] == 'go':
        find_dir = command.split()[1:4]
        dir_room = ' '.join(find_dir)
        if dir_room in current_room:
            current_room = rooms[current_room[dir_room]]
        else:
            # bad movement
            print("You can't go that way.")
    # gather items
    elif command.split()[0] == 'get':
        find_item = command.split()[1:4]
        item = ' '.join(find_item)
        if item in current_room['contents']:
            current_room['contents'].remove(item)
            inventory.append(item)
        else:
            print("You don't see a {}.".format(item))
    # quit game
    elif command == "exit":
        current_room = rooms[current_room['exit']]
    if command == 'yes' and current_room == rooms['exit']:
        break
    elif command == 'no' and current_room == rooms['exit']:
        current_room = rooms['Airlock']
    # showdown
    victories = 0
    if current_room == rooms['Engineering']:
        print()
        print('You are in the {}.'.format(current_room['name']))
        print(current_room['text'])
        print(current_room['exits'])
        if 'Space Suit' in inventory and victories < 1:
            space_suit()
            victories += 1
        else:
            space_suit()
            break
        if 'Oxygen tank' in inventory and victories < 2:
            oxygen_tank()
            victories += 1
        else:
            oxygen_tank()
            break
        if 'Electric baton' in inventory and victories < 3:
            electric_baton()
            victories += 1
        else:
            electric_baton()
            break
        if 'Fusion core key' in inventory and victories < 4:
            core_key()
            victories += 1
        else:
            core_key()
            break
        if 'Engine initiation code' in inventory and victories < 5:
            engine_code()
            victories += 1
        else:
            engine_code()
            break
        if 'Safety override' in inventory and victories < 6:
            safety_chip()
            victories += 1
        else:
            safety_chip()
            break
        if victories == 6:
            print('Winner')
            break
