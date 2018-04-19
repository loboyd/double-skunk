import functionality as func

class Player(object):
    """Class describing a player including name (input argument), score and hand

    hand display format:

    | A | 7 | 3 | 2 | J | J |
    | H | C | S | D | D | H |
    -------------------------
    | 1 | 2 | 3 | 4 | 5 | 6 |

    """

    def __init__(self, name):
        self.score = 0
        self.hand = []
        self.name = name

    def discard(self):
        """This method prompts the user to choose discards."""
        print("\n{0} ({1}): ".format(self.name, self.score))
        print("Which cards would you like to discard?")
        print("Please input two integers separated by a space.")

        self.print_hand()

        # get valid discards
        discards = '0 0'
        while len(discards) < 3 or discards[0] not in '123456' or discards[2] \
        not in '123456' or discards[1] is not ' ' or discards[0] == discards[2]:
            if discards is not '0 0':
                print("Sorry. That was an invalid input. Please retry.\n")
            discards = raw_input('selected cards: ').strip()
        discards = sorted([int(i)-1 for i in discards.split(' ')])  # convert to int and 0-indexed
        # discards = sorted(map(int, discards.split(' ')))

        # remove discards from player's hand
         # self.hand = self.hand[:discards[0] - 1] + self.hand [discards[0]:discards[1] - 1] \
         #  + self.hand[discards[1]:]
        # another way of doing the above:
        discards = discards[::-1]  # reverse list so del works properly for both discards
        for discard in discards:
            del self.hand[discard]

        return discards

    def print_hand(self):
        """Print hand in easy-to-read way"""
        # print card rank line
        for card in self.hand:
            print("| {0}".format(func.ranks[func.card_rank(card)])),
        print('|')

        # print card suite line
        for card in self.hand:
            print("| {0}".format(func.suites[func.card_suite(card)])),
        print('|')

        # print separater and hand indices
        if len(self.hand) == 6:
            print('-'*25)
        else:
            print('-'*17)
        for i in xrange(1, len(self.hand) + 1):
            print("| {0}".format(str(i))),
        print('|\n')

    def peg(self):
        """TO-BE-COMPLETED"""
        return 0
