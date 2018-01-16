"""
Simple implementation of cribbage which might ultimately be deployed for use by
David and me over the internet.

(The actually beginning date of this project is a few days earlier than this:)
01 - 11 - 2017  --  L. Boyd

"""

# modules
import random

# general game tables
suites = ['S', 'D', 'C', 'H']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K']

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
        print "\n{0} ({1}): ".format(self.name, self.score)
        print "Which cards would you like to discard?"
        print "Please input two integers separated by a space."

        self.print_hand()

        # get valid discards
        discards = '0 0'
        while len(discards) < 3 or discards[0] not in '123456' or discards[2] \
        not in '123456' or discards[1] is not ' ' or discards[0] == discards[2]:
            if discards is not '0 0':
                print "Sorry. That was an invalid input. Please retry.\n"
            discards = raw_input('selected cards: ').strip()
        discards = sorted(map(int, discards.split(' ')))

        # remove discards from player's hand
         # self.hand = self.hand[:discards[0] - 1] + self.hand [discards[0]:discards[1] - 1] \
         #  + self.hand[discards[1]:]
        # another way of doing the above:
        for discard in discards:
            del a[discard]


        return discards

    def print_hand(self):
        """Print hand in easy-to-read way"""
        # print card rank line
        for card in self.hand:
            print "| {0}".format(ranks[card_rank(card)]),
        print '|'

        # print card suite line
        for card in self.hand:
            print "| {0}".format(suites[card_suite(card)]),
        print '|'

        # print separater and hand indices
        if len(self.hand) == 6:
            print '-'*25
        else:
            print '-'*17
        for i in xrange(1, len(self.hand) + 1):
            print "| {0}".format(str(i)),
        print '|\n'


def deal():
    """Get random sample of 13 cards represented by integers between 0 and 51;
    first six cards are Alice's hand, next six are Bob's hand, last is starter card"""
    temp = random.sample(range(52), 13)
    hand1 = temp[:6]
    hand2 = temp[6:12]
    starter = temp[12]
    return sorted(hand1), sorted(hand2), starter


def card_suite(card):
    """Return the suite index of a card (integer represented)"""
    return card % 4


def card_rank(card):
    """Return the rank index of a card (integer represented)"""
    return card / 4


def card_string(card):
    """Return a string describing a card such as 6 H for six of hearts"""
    return "{0}-{1}".format(ranks[card_rank(card)], suites[card_suite(card)])

############################## GAME PLAY #######################################
# initialize players
alice = Player('Alice')
bob = Player('Bob')

# generate (uniformly) random boolean to determine first dealer
if random.random() < 0.5:
    dealer = alice
else:
    dealer = bob
print "{0} gets the first crib!\n".format(dealer.name)

# per-game
"""NOT COMPLETE"""
while True:
    # deal
    alice.hand, bob.hand, starter_card = deal()

    # discard
    crib = alice.discard() + bob.discard()

    # reveal (display the starter card to players)
    # temporary solution for building functionality
    print "\nSTARTER CARD: {0}".format(card_string(starter_card))

    # the play (pegging)
    table = []
    to_peg = dealer
    while len(table) < 8:
        # update table
        table.append(to_peg.peg)

        # update player score

        # if player won, break

    # the show

# TODO:
# - come up with a nice way of sorting the hands (It would be really nice if the
#   numbers representing the cards happened to share the preferred ordering of
#   the cards -- this way, the native sorted() could be used.) EDIT -- I think
#   this is working now, but it should probably be double-checked
# - possbily place the actual gameplay and the overhead in separate PY files
# - finish the pegging and play code
# - figure out how to count points (both play and show)
