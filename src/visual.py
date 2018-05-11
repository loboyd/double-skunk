import functionality as func

def print_user_commands(commands):
    """Print list of user commands and their descriptions"""
    for c in commands:
        print("{0}{1}".format(c, commands[c]))
    print

def clear_screen():
    """Clears the console.

    UPDATE TO BE CROSS-PLATFORM"""

    import os
    os.system('clear')

def print_title_bar():
    """Prints the double-skunk title bar"""
    print("====DOUBLE-SKUNK=============================")

def print_score_bar(slf_score, opp_score):
    """Prints the score bar with opponent on the left, self on the right"""
    print("OPPONENT: |{0:3}|                    YOU: |{1:3}|".format(
        opp_score, slf_score))

def first_dealer_message(dealer):
    """Display message for informing the player of the first dealer"""
    clear_screen()
    print_title_bar()
    print("\n{} will be the first dealer.".format(
        "YOU" if dealer else "YOUR OPPONENT"))
    usr = raw_input("\n\nPress ENTER to continue to the game.")
    print("\nWAITING FOR OPPONENT...")

def go_message():
    """Alert player they must say ``GO``"""
    print("No playable cards. You must say \"GO\".")
    raw_input("Please press ENTER")

def print_hand(cards, crib=0, index=1):
    """Print hand up to six cards with rank, suite, and hand index in
    the following format:

    | A || 2 || 3 || X || J || Q |
    | C || H || D || D || S || H |
    ------------------------------
      1    2    3    4    5    6

    """
    n = len(cards)

    # set up line strings
    rank_line  = ''
    suite_line = ''
    div_line   = ''
    index_line = ''

    if n > 0:
        # build line strings
        ct = 1
        for c in cards:
            rank_line  += "| {0} |".format(func.card_rank_string(c))
            suite_line += "| {0} |".format(func.card_suite_string(c))
            div_line   += "-----"
            index_line += "  {0}  ".format(ct)
            ct += 1

    # include crib
    if crib:
        crib_buffer = ' '*(35-len(rank_line))
        rank_line  += crib_buffer + "| _ ||||"
        suite_line += crib_buffer + "|   ||||"


    # print them
    print('\n')
    print(rank_line)
    print(suite_line)
    if index:
        print(div_line)
        print(index_line)

def print_table(cards, mask, starter):
    """Print the cards which have been played in pegging; use the mask
    to determine the ownership of the cards"""
    n = len(cards)

    # set up line strings
    starter_line = ' '*44 + "STARTER"
    top_line = ''
    mid_line = ''
    bot_line = ''

    if n > 0:
        # pair card with ownership
        cards = zip(cards, mask)

        # build line strings with position based on ownership
        for card, owner in cards:
            # build card pieces
            card_top = "| {0} |".format(func.card_rank_string(card))
            card_bot = "| {0} |".format(func.card_suite_string(card))

            if owner:
                top_line += "     "
                mid_line += card_top
                bot_line += card_bot
            else:
                top_line += card_top
                mid_line += card_bot
                bot_line += "     "

    # include starter card
    starter_buffer = ' '*(45-len(top_line))
    top_line += starter_buffer + "| {0} |".format(func.card_rank_string(starter))
    mid_line += starter_buffer + "| {0} |".format(func.card_suite_string(starter))

    print('\n')
    print(starter_line)
    print(top_line)
    print(mid_line)
    print(bot_line)
    print('\n')

# def display_all_hand_counts(dealer, slf_hand, opp_hand, crib, starter,
#     slf_score, opp_score):
#     """Display all hands with their total point counts in the
#     proper order"""
#     # collect hands and description strings and establish order
#     hands = [slf_hand, opp_hand, crib]
#     strings = ["YOUR HAND", "OPPONENT'S HAND"]
#     if dealer:
#         ind = [1, 0, 2]
#         strings.append("YOUR CRIB")
#     else:
#         ind = [0, 1, 2]
#         strings.append("OPPONENT'S CRIB")
# 
#     # loop over hands and display
#     for i in ind:
#         clear_screen()
#         print_title_bar()
# 
#         # calculate score and update score bar
#         score_tmp = func.score_hand(hands[i], starter)
#         print_score_bar(slf_score, opp_score)
#         
#         # display hand count to user
#         print("\n{0}".format(strings[i]))
#         print("SCORE: {0:3}".format(score_tmp))
#         print_hand(hands[i])
#         raw_input("Press ENTER to continue.")
# 
#     return slf_score, opp_score

def display_all_hand_counts(dealer, slf_hand, opp_hand, crib, starter,
    slf_score, opp_score):
    """"""
    if dealer:
        hands   = [opp_hand, slf_hand, crib]
        owner   = [False,    True,     True]
        strings = ["OPPONENT'S HAND", "YOUR HAND", "YOUR CRIB"]
    else:
        hands   = [slf_hand, opp_hand, crib]
        owner   = [True,     False,    False]
        strings = ["YOUR HAND", "OPPONENT'S HAND", "OPPONENT'S CRIB"]

    # loop over all hands
    for i in xrange(len(hands)):
        hand_score = func.score_hand(hands[i], starter)
        if owner[i]:
            slf_score += hand_score
        else:
            opp_score += hand_score

        clear_screen()
        print_title_bar()
        print_score_bar(slf_score, opp_score)

        print("\n{0}".format(strings[i]))
        print("SCORE: {0:3}".format(hand_score))
        print_hand(hands[i])
        raw_input("Press ENTER to continue.")

    return slf_score, opp_score
