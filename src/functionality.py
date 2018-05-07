import random
import peer
import visual

# general game tables
suites = ['S', 'D', 'C', 'H']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K']

def deal(dealer, opp_addr):
    """Get random sample of 13 cards; the first six cards are the dealer's
    hand, the next six are the other player's hand, last is starter card"""
    # establish seed
    if dealer:
        seed = str(random.random())
        peer.send(opp_addr, str(seed))
    else:
        seed = peer.recv(opp_addr)

    random.seed(float(seed))

    temp = random.sample(range(52), 13)
    if dealer:
        slf_hand = temp[:6]
        opp_hand = temp[6:12]
    else:
        slf_hand = temp[6:12]
        opp_hand = temp[:6]
    starter = temp[12]

    return sorted(slf_hand), sorted(opp_hand), starter

def card_suite(card):
    """Return the suite index of a card (integer represented)

    TODO:
    add `return string` capability with st=None input"""
    return card % 4

def card_rank(card):
    """Return the rank index of a card (integer represented)

    TODO:
    add `return string` capability with st=None input"""
    return card / 4

def card_value(card):
    """Return the point value of a card (integer represented)"""
    if card_rank(card) == 10 or card_rank(card) == 11 or card_rank(card) == 12:
        return 10
    else:
        # +1 because ranks are 1 larger than their indices
        return card_rank(card) + 1

def card_rank_string(card):
    """Return a string describing the rank of a card or underscore for
    face-down"""
    if card == -1:
        return '_'
    return ranks[card_rank(card)]

def card_suite_string(card):
    """Return a string describing the suite of a card or blank space
    for face-down"""
    if card == -1:
        return ' '
    return suites[card_suite(card)]

def select_cards(hand):
    """Get user input and remove selected cards from hand (prompt
    must be handled outside)"""
    usr = raw_input()
    usr = [int(s) - 1 for s in usr.split(' ')]  # -1 because hand is 1-indexed
    selection = [hand[i] for i in usr]

    for i in sorted(usr, reverse=True):
        del hand[i]

    return selection, hand

def discard(hand, dealer):
    """Display hand and return user selected discards and updated hand"""
    visual.clear_screen()
    visual.print_title_bar()

    print("\nSelect two cards to discard.")
    print("{0} the crib.\n".format('You have' if dealer else 'Your opponent has'))

    visual.print_hand(hand)

    discards, hand = select_cards(hand)

    return discards, hand


def get_crib(dealer, hand, addr):
    """Return crib after performing discard and exchanging card info
    with peer"""
    slf_crib_cards, hand = discard(hand, dealer)
    slf_crib_cards_string = "{0} {1}".format(slf_crib_cards[0], slf_crib_cards[1])

    opp_crib_cards_string = peer.exchange(addr, slf_crib_cards_string)
    opp_crib_cards = opp_crib_cards_string.split(' ')

    crib = sorted(slf_crib_cards + opp_crib_cards)
    return crib, hand

def valid_play_exists(hand, table_value_sum):
    """Determine whether or not a valid play exists given a
    hand paired with the sum of the values of the table"""
    if hand:
        return min(map(card_value, hand)) + table_value_sum <= 31
    return False

def score_play(table):
    """Given a table of played cards, return points earned by the most
    recently played card"""
    n = len(table)
    points = 0

    # count pairs/triples/quadruples
    i = -2
    while abs(i) < n+1 and card_rank(table[i]) == card_rank(table[-1]):
        # twice the number of cards similar to the last played card
        points += 2*(abs(i)-1)
        i -= 1

    # check fifteen
    if sum([card_rank(c) for c in table]) == 15:
        points += 2

    # check thirty-one
    if sum([card_rank(c) for c in table]) == 31:
        points += 2

    # check run(s)
    # -2 because must runs must have 3 cards
    for i in xrange(-n,-2):
        tmp = table[i:]
        if is_run(tmp):
            points += len(tmp)

    return points

def is_run(cards):
    """Determine whether or not three cards constitute a run"""
    n = len(cards)
    if 3 <= n <= 5:
        ranks = sorted([card_rank(c) for c in cards])
        return ranks == range(min(ranks),max(ranks)+1)
    return False

def score_hand(hand, starter, crib=False):
    """Returns the total score of a starter card paired with a hand
    NOT COMPLETED
    things to count:
        - fifteen(s) - broken
        - run(s)     - done
        - pair(s)    - done
        - flush      - done
        - nobs       - done
    """
    return score_fifteens(hand, starter)    \
         + score_runs(hand, starter)        \
         + score_pairs(hand, starter)       \
         + score_flush(hand, starter, crib) \
         + score_nobs(hand, starter)

def score_fifteens(hand, starter):
    """Return the number of points earned by the fifteens in a
    hand paired with a starter card

    NOTE: This structure of this function copied directly from
    score_runs() below, so there is probably a better way to do
    either or both of the functions."""
    # add the starter to the hand
    hand.append(starter)
    hand = sorted(hand)
    hand = map(card_value, hand)
    n = len(hand)
    points = 0

    # check for five card fifteen
    if sum(hand) == 15:
        # smaller fifteens are not possible if a 5-card fifteen exists
        print('5 card')
        return 2

    # loop over all possible quadruples
    for i in xrange(n):
        tmp = hand[:i] + hand[i+1:]
        if sum(tmp) == 15:
            points += 2
            print('4 card')

    # loop over all possible triples and check for fifteen-ship
    for i in xrange(n-2):
        for j in xrange(i+1, n-1):
            for k in xrange(j+1, n):
                # there is probably a nicer way to do this...
                tmp = [hand[i], hand[j], hand[k]]
                if sum(tmp) == 15:
                    points += 2
                    print('3 card')

    # loop over all possible tuples and check for fifteen-ship
    for i in xrange(n-1):
        for j in xrange(i+1,n):
            tmp = [hand[i], hand[j]]
            if sum(tmp) == 15:
                points += 2
                print('2 card')

    return points

#def score_fifteens(hand, starter, total=15):
#    """Return number of unique fifteen-pairs of a hand paired with a
#    starter card
#    WRITE UNIT TEST FOR THIS"""
#    # include the starter card in the hand if recursion depth is 0
#    if starter != -1:
#        hand = [starter] + hand
#        hand = map(card_value, hand)
#
#    # base case
#    if len(hand) == 1:
#        if total == hand[0]:
#            return 1
#        else:
#            return 0
#
#    # recursively call fifteens() on the cases with and without using
#    # the first card
#    else:
#        return score_fifteens(hand[1:], -1, total-hand[0]) \
#             + score_fifteens(hand[1:], -1, total)

def score_runs(hand, starter=None):
    """Return the number of points earned by the runs of a hand
    paired with a starter card"""
    # add the starter to the hand
    if starter:
        hand.append(starter)
    hand = sorted(hand)
    n = len(hand)
    points = 0

    # check for five card run
    if is_run(hand):
        # smaller runs are not possible if a 5-run exists
        return 5

    # loop over all possible quadruples
    for i in xrange(n):
        tmp = hand[:i] + hand[i+1:]
        if is_run(tmp):
            points += 4

    # 3-runs are not possible if a 4-run exists
    if points:
        return points

    # loop over all possible triples and check for run-ship
    for i in xrange(n-2):
        for j in xrange(i+1, n-1):
            for k in xrange(j+1, n):
                # there is probably a nicer way to do this...
                tmp = [hand[i], hand[j], hand[k]]
                if is_run(tmp):
                    points += 3

    return points

def score_pairs(hand, starter):
    """Return number of points earned by pairs in a hand paired
    with a starter card
    WRITE UNIT TEST FOR THIS"""
    # add the starter to the hand
    hand += [starter]

    points = 0

    n = len(hand)
    for i in xrange(n-1):
        for j in xrange(i+1, n):
            if hand[i] == hand[j]:
                points += 2
    return points

def score_flush(hand, starter, crib=False):
    """Return number of points earned by a flush of a hand paired
    with a starter card"""
    n = len(hand)
    if n < 4:
        return 0

    suites = [card_suite(c) for c in hand]
    starter_suite = card_suite(starter)
    combined_suites = suites + [starter_suite]

    # set is used to check all suites are the same
    if len(set(combined_suites)) == 1:
        return 5

    elif not crib and len(set(suites)) == 1:
        return 4
    return 0

def score_nobs(hand, starter):
    """Return number of points earned by nobs in hand paired with a
    starter card
    WRITE UNIT TEST FOR THIS"""
    starter_suite = card_suite(starter)
    for card in hand:
        if card_rank_string(card) == 'J' and card_suite(card) == starter_suite:
            return 1
    return 0

