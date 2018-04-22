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

def print_hand(hand):
    """Print hand up to six cards with rank, suite, and hand index in
    the following format:

    | A | 2 | 3 | X | J | Q |
    | C | H | D | D | S | H |
    -------------------------
    | 1 | 2 | 3 | 4 | 5 | 6 |

    """
    n = len(hand)
    if n == 0:
        print "\n\n\n\n"
    else:
        # build line strings
        rank_line  = "| "
        suite_line = "| "
        div_line   = "-"
        index_line = "| "
        ct = 1
        for c in hand:
            rank_line  += "{0} | ".format(func.card_rank_string(c))
            suite_line += "{0} | ".format(func.card_suite_string(c))
            div_line   += "----"
            index_line += "{0} | ".format(ct)
            ct += 1

        # print them
        print"\n"
        print(rank_line)
        print(suite_line)
        print(div_line)
        print(index_line)
        print "\n"

