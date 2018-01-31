"""
This file contains the main game loop.
"""

import random
import functionality as func
import player

user_commands = {
    'add......': 'add a new friend',
    'friends..': 'see friend list',
    'name.....': 'edit your username',
    'new......': 'enter new game',
    'help.....': 'see this list of commands',
    'quit.....': 'quit game'
}


def print_user_commands():
    """Print list of user commands and their descriptions"""
    for c in user_commands:
        print("{0}{1}".format(c, user_commands[c]))
    print


def clear_screen():
    """Clears the console. 
    
    UPDATE TO BE CROSS-PLATFORM"""
    
    import os
    os.system('clear')


def print_title_bar():
    """Prints the double-skunk title bar"""
    print("====DOUBLE-SKUNK=============================")


def exit_client():
    """Say goodbye and exit client"""
    clear_screen()
    print_title_bar()
    print("\nSee you next time!\n")
    exit()


def play_game():
    """Facilitates gameplay between two peers -- friends or public
    
    NOT CURRENTLY A SECURE AND TRUSTLESS IMPLEMENTATION
    """
    raise NotImplementError  # temporary
    return None              # also temporary
    
    slf_score = 0
    opp_score = 0
    
    # "play against friend or on public network?"
    
    # establish connection with socket(s)
    
    # determine first dealer (THIS IS NOT SECURE AND TRUSTLESS)
    first_pass = True
    while first_pass or opp_rand == slf_rand:
        first_pass == False
        opp_rand = get_random_from_opponent()  # dummy function; not yet implemented
        slf_rand = random.random()
    
    if opp_rand > slf_rand:
        dealer = 1
    else:
        dealer = 0
    
    """    
    game loop
      - deal cards
      - discard crib cards
      - reveal starter card
      - the play (pegging phase)
      - count hands and crib
    """
    

    # deal cards (THIS IS NOT SECURE AND TRUSTLESS)
    # generate seed to ensure identical shuffles
    


def add_friend():
    """Saves a new friend to the friend list"""
    raise NotImplementedError


def view_friends_list():
    """prints friends list to screen"""
    raise NotImplementedError


def edit_user_name():
    """Allows user to edit public username"""
    raise NotImplementedError


def main():
    # entry statement
    clear_screen()
    print_title_bar()
    print("\nWelcome to double-skunk!")
    print("Enter the following commands to navigate:\n")
    print_user_commands()
    
    # client loop
    while True:
        usr = raw_input("")
        clear_screen()
        print_title_bar()
        print
    
        if usr == 'add':
            # add friend
            print("functionality yet to be added")
            print("enter \"help\" to go back\n")
        elif usr == 'friends':
            # print list of friends
            print("functionality yet to be added")
            print("enter \"help\" to go back\n")
        elif usr == 'name':
            # edit/set username
            print("functionality yet to be added")
            print("enter \"help\" to go back\n")
        elif usr == 'new':
            # enter new game
            print("functionality yet to be added")
            print("enter \"help\" to go back\n")
        elif usr == 'help':
            print
            print_user_commands()
        elif usr == 'quit' or usr == 'exit':
            exit_client()
        else:
            print('That was an invalid entry. Enter \'help\' to see the available commands.')


if __name__ == "__main__":
    main()














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
