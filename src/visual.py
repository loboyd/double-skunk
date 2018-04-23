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

def first_dealer_message(dealer):
    """Display message for informing the player of the first dealer"""
    clear_screen()
    print_title_bar()
    print("\n{} will be the first dealer.".format("YOU" if dealer else "YOUR OPPONENT"))
    usr = raw_input("\n\nPress ENTER to continue to the game.")
    print("\nWAITING FOR OPPONENT...")

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
    print('\n')

def print_table(cards, mask, starter):
    """Print the cards which have been played in pegging; use the mask to determine
    the ownership of the cards"""
    n = len(cards)

    # set up line strings
    starter_line = ' '*44 + "STARTER"
    top_line = ''
    mid_line = ''
    bot_line = ''

    if n > 0:
        cards = zip(cards, mask)

        # build line strings with position based on ownership
        for c in cards:
            # build card pieces
            card_top = "| {0} |".format(func.card_rank_string(c[0]))
            card_bot = "| {0} |".format(func.card_suite_string(c[0]))

            if c[1]:
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
