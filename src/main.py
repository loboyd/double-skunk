"""
This file contains the main game loop.
"""

import random
import functionality as func
import player


# ==============================================================================
# - P2P OUTLINE/DESIGN ---------------------------------------------------------
# ==============================================================================


# there will probably be something of a "main menu" where users can start a 
# game, update their user info (display name, etc.), add a new peer manually

# find/connect to peer

# exchange info (username, random seed info, etc.)








# ================================================================
# - OLD TESTING CODE (PRE-P2P DECISION) --------------------------
# ================================================================

# initialize players
# alice = player.Player('Alice')
# bob = player.Player('Bob')
#
# # generate (uniformly) random boolean to determine first dealer
# if random.random() < 0.5:
#     dealer = alice
# else:
#     dealer = bob
# print "{0} gets the first crib!\n".format(dealer.name)
#
# # per-game
# """NOT COMPLETE: eventually this will work between two connected computers instead
# of working with a single console"""
# while True:
#     # deal
#     alice.hand, bob.hand, starter_card = func.deal()
#
#     # discard
#     crib = alice.discard() + bob.discard()
#
#     # reveal (display the starter card to players)
#     # temporary solution for building functionality
#     print "\nSTARTER CARD: {0}".format(func.card_string(starter_card))
#
#     # the play (pegging)
#     table = []
#     to_peg = dealer
#     while len(table) < 8:
#         # update table
#         table.append(to_peg.peg)
#
#         # update player score
#
#         # if player won, break
#
#     # the show
