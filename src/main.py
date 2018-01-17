"""
This file contains the main game loop.
"""

import random

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
"""NOT COMPLETE: eventually this will work between two connected computers instead
of working with a single console"""
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
# - consider breaking this file into "player," "functionality," and "main" files
# - finish "play" and "show" code
# - write a function to count points
# - work on P2P communication over the web (either with library at socket level)
# - write some stand-only documentation (not just comments)
# - further specify the design (in documentation)
# - add some testing
# - finish todo list (probably move the todo list to its own file)
