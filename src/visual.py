import functionality as func
import curses

def menu(stdscr, items, message='double-skunk'):
    """Get user selection from curses-built menu;
       return index to items list

       * based on a code example from github.com/bmgxyz"""
    curses.curs_set(False)
    stdscr.clear()

    n_items = len(items)

    # render message
    menu_height = 1 + 2*n_items
    message_line = (curses.LINES - menu_height) // 2
    message_col  = (curses.COLS - len(message)) // 2
    stdscr.addstr(message_line, message_col, message)

    # render items
    current_line = message_line
    option_lines = [None]*n_items
    for i, option in enumerate(items):
        current_line += 2
        option_lines[i] = current_line  # store line for option
        current_col = (curses.COLS - len(option)) // 2
        stdscr.addstr(current_line, current_col, option)

    # start cursor on the first option
    index = 0
    while True:
        index = index % n_items
        left_col  = curses.COLS // 2 - 8
        right_col = curses.COLS // 2 + 8
        current_line = option_lines[index]

        # display selection indicators
        stdscr.addstr(current_line, left_col, '>')
        stdscr.addstr(current_line, right_col, '<')
        stdscr.refresh()

        # get user input
        c = stdscr.getkey()
        if c == '\n':
            return index
        elif c in ['KEY_UP', 'KEY_DOWN']:
            stdscr.addstr(current_line, left_col, ' ')
            stdscr.addstr(current_line, right_col, ' ')
            index += (-1 if c == 'KEY_UP' else 1)

def usr_input(stdscr, line, col, prompt, max_length=20):
    """Get user input with curses"""
    curses.echo()
    stdscr.addstr(line, col, prompt)
    stdscr.addstr(line+1, col, '> ')
    stdscr.refresh()
    return stdscr.getstr(line+1, col+2, max_length)

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

def first_dealer_message(stdscr, dealer):
    """Display message for informing the player of the first dealer"""
    # curses.curs_set(False)
    stdscr.clear()

    # set message
    if dealer:
        message = 'YOU will be the first dealer'
    else:
        message = 'YOUR OPPONENT will be the first dealer'

    # render message
    height = 4
    message_line = (curses.LINES - height) // 2
    message_col  = (curses.COLS - len(message)) // 2

    stdscr.addstr(message_line, message_col, message)

    # put ``> continue <`` with blinking cursor here eventually
    while True:
        c = stdscr.getkey()
        if c == '\n':
            break

#def first_dealer_message(dealer):
    #"""Display message for informing the player of the first dealer"""
    # clear_screen()
    # print_title_bar()
    # print("\n{} will be the first dealer.".format(
    #     "YOU" if dealer else "YOUR OPPONENT"))
    # usr = raw_input("\n\nPress ENTER to continue to the game.")
    # print("\nWAITING FOR OPPONENT...")
    # curses.wrapper(first_dealer_message_curses, dealer)

def go_message():
    """Alert player they must say ``GO``"""
    print("No playable cards. You must say \"GO\".")
    raw_input("Please press ENTER")

def print_hand(cards, crib=False, index=1, starter=None):
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

    # include starter card
    if starter:
        starter_buffer = ' '*(35-len(rank_line))
        rank_line  += starter_buffer + "| {0} |".format(func.card_rank_string(starter))
        suite_line += starter_buffer + "| {0} |S".format(func.card_suite_string(starter))

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
        print_hand(hands[i], index=False, starter=starter)
        raw_input("\nPress ENTER to continue.")

    print("WAITING FOR OPPONENT...")

    return slf_score, opp_score
