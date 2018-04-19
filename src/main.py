"""
This file contains the main game loop.
"""

import random
import functionality as func
import player
import peer

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

    slf_score = 0
    opp_score = 0

    # get peer address
    host = peer.get_opp_ip()  # dummy function; not yet implemented
    port = 55693
    opp_addr = (host, port)

    # determine first dealer (THIS IS NOT SECURE AND TRUSTLESS)
    slf_draw = random.random()
    opp_draw = peer.exchange(str(opp_addr), str(slf_draw))
    dealer = 0 if int(slf_draw) < int(opp_draw) else 1

    game_over = 0

    # main game loop
    while not game_over:
        # deal cards
        hand, starter_card = functionality.deal(dealer, opp_addr)

        # perform discard
        crib = functionality.get_crib(dealer, hand, opp_addr)

        # reveal starter
        reveal_starter(starter_card)

        # pegging phase
        slf_score, opp_score = pegging_play(dealer, slf_score, opp_score, opp_addr)
        if check_game_over(slf_score, opp_score):
            break

        # count hands and crib
        slf_score, opp_score = functionality.count_hands(dealer, hand, crib)
        if check_game_over(slf_score, opp_score):
            break


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
