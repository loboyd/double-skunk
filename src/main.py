"""
This file contains the main game loop.
"""

import random
import functionality as func
import peer
import visual

user_commands = {
    'add......': 'add a new friend',
    'friends..': 'see friend list',
    'name.....': 'edit your username',
    'new......': 'enter new game',
    'help.....': 'see this list of commands',
    'quit.....': 'quit game'
}

def exit_client():
    """Say goodbye and exit client"""
    visual.clear_screen()
    visual.print_title_bar()
    print("\nSee you next time!\n")
    exit()

def pegging_play(hand, starter_card, slf_score, opp_score, addr, dealer):
    """Facilitates pegging phase for one round of the dealing cycle"""
    table = []       # store played cards
    owner_mask = []  # store card ownership information
    n_opp_cards = 4
    opp_crib = not dealer  # dealer's opponent always has crib
    to_play  = not dealer  # and is also first to play

    done_pegging = 0
    while not done_pegging:
        visual.clear_screen()
        visual.print_title_bar()

        visual.print_hand([-1]*n_opp_cards, index=0, crib=opp_crib)

        visual.print_table(table, owner_mask, starter_card)

        if to_play:
            print("PLEASE PLAY A CARD")
        else:
            print("WAITING FOR OPPONENT...")

        visual.print_hand(hand, crib=dealer)

        # get played card or go message
        go = False
        if to_play:
            table_points = sum(map(func.card_value, table))
            min_card = min(map(func.card_value, hand))
            if table_points + min_card > 31:
                visual.go_message();
                go = 1
                play_card = '-1'  # go card
            else:
                play_card, hand = func.select_cards(hand)
                play_card = play_card[0]
            peer.send(addr, str(play_card))
        else:
            play_card = int(peer.recv(addr))
            if play_card == '-1':
                go = 1
            else:
                n_opp_cards -= 1

        # update table
        if not go:
            table.append(play_card)
            owner_mask.append(to_play)

            # update score
            play_score = func.score_play(table)
        if to_play:
            slf_score += play_score
            if slf_score >= 121:
                done_pegging = 1
        else:
            opp_score += play_score
            if opp_score >= 121:
                done_pegging = 1

        # pass play between players
        to_play = not to_play

    return slf_score, opp_score

def play_game():
    """Facilitates gameplay between two peers

    NOT CURRENTLY A SECURE AND TRUSTLESS IMPLEMENTATION
    """

    slf_score = 0
    opp_score = 0

    # get peer address
    host = peer.get_peer_ip()
    port = 55693
    opp_addr = (host, port)

    # determine first dealer (THIS IS NOT SECURE AND TRUSTLESS)
    slf_draw = random.random()
    opp_draw = peer.exchange(opp_addr, str(slf_draw))
    dealer = 0 if float(slf_draw) < float(opp_draw) else 1

    visual.first_dealer_message(dealer)

    # main game loop
    game_over = 0
    while not game_over:
        # deal cards (ALSO NOT SECURE AND TRUSTLESS)
        slf_hand, opp_hand, starter_card = func.deal(dealer, opp_addr)

        # perform discard
        crib, slf_hand = func.get_crib(dealer, slf_hand, opp_addr)

        # pegging phase
        slf_score, opp_score = pegging_play(slf_hand, starter_card,
            slf_score, opp_score, opp_addr, dealer)
        if check_game_over(slf_score, opp_score):
            break

        # count hands and crib
        slf_score, opp_score = func.count_hands(dealer, slf_hand, opp_hand, crib)
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
    visual.clear_screen()
    visual.print_title_bar()
    print("\nWelcome to double-skunk!")
    print("Enter the following commands to navigate:\n")
    visual.print_user_commands(user_commands)

    # client loop
    while True:
        usr = raw_input("")
        visual.clear_screen()
        visual.print_title_bar()
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
            play_game()
        elif usr == 'help':
            print
            visual.print_user_commands(user_commands)
        elif usr == 'quit' or usr == 'exit':
            exit_client()
        else:
            print('That was an invalid entry. Enter \'help\' to see the available commands.')

if __name__ == "__main__":
    main()

