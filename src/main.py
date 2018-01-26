"""
This file contains the main game loop.
"""

import random
import functionality as func
import player

commands = {
    'add......': 'add a new friend',
    'friends..': 'see friend list',
    'name.....': 'edit your username',
    'new......': 'enter new game',
    'help.....': 'see this list of commands',
    'quit.....': 'quit game'
}


def print_commands():
    for c in commands:
        print("{0}{1}".format(c, commands[c]))
    print


def clearscreen():
    """Clears the console. UPDATE TO BE CROSS-PLATFORM"""
    import os
    os.system('clear')


# entry statement
clearscreen()
print("Welcome to double-skunk!")
print("Enter the following commands to navigate:\n")
print_commands()

# main client loop
usr = raw_input()
while usr != 'quit':
    if usr == 'add':
        pass
        # add friend
    elif usr == 'friends':
        # print list of friends
        pass
    elif usr == 'name':
        # edit/set username
        pass
    elif usr == 'new':
        # enter new game
        pass
    elif usr == 'help':
        print
        print_commands()
    elif usr == 'quit' or usr == 'exit':
        exit_game()
    else:
        print('That was an invalid entry. Enter \'help\' to see the available commands.')
    
    usr = raw_input()


# exit statement
def exit_game():
    print("\nSee you next time!")
    exit()
















# THE OUTLINE BELOW WILL BE USEFUL LATER ON

# ==============================================================================
# - P2P OUTLINE/DESIGN ---------------------------------------------------------
# ==============================================================================


# there will probably be something of a "main menu" where users can start a 
# game, update their user info (display name, etc.), add a new peer manually

# find/connect to peer

# exchange info (username and whatever else)

# perform "coin flip" for first dealer (this is not trivial)

# game loop

    # deal cards
    
    # discard to crib

    # pegging phase
    
    # reveal starter card
    
    # count hands
