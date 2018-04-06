import random

# general game tables
suites = ['S', 'D', 'C', 'H']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K']


def deal():
    """Get random sample of 13 cards represented by integers between 0 and 51;
    first six cards are Alice's hand, next six are Bob's hand, last is starter card"""
    temp = random.sample(range(52), 13)
    hand1 = temp[:6]
    hand2 = temp[6:12]
    starter = temp[12]
    return sorted(hand1), sorted(hand2), starter


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
        return card_rank(card) + 1  # +1 because ranks are 1 larger than their indices


def card_string(card):
    """Return a string describing a card such as 6 H for six of hearts"""
    return "{0}-{1}".format(ranks[card_rank(card)], suites[card_suite(card)])


def score_hand(hand, starter):
    """Returns the total score of a starter card paired with a hand
    NOT COMPLETED
    things to count:
        - fifteen(s) - done
        - run(s)
        - pair(s)    - done
        - flush
        - nobs       - done
    """
    # # point values for each score "structure"
    # fifteen_point_val = 2
    # run_point_val     = {0:0, 3:3, 4:4, 5:5}  # length-of-run:score pairs
    # pair_point_val    = 2
    # flush_point_val   = {0:0, 4:4, 5:5}       # length-of-flush:score pairs
    # nobs_point_val    = 2
    #
    # fifteen_score = fifteen_point_val * count_fifteens(hand, starter)
    # run_score = 0  # 0 is a place holder
    #
    # return fifteen_score*count_fifteens(hand, starter) + \
    #         run_score[count_run(hand, starter)] + \
    #         count_pairs*count_pairs(hand, starter) + \
    #         flush_score[count_flush(hand, starter)] + \
    #         nobs_score*count_nobs(hand, starter)


def count_fifteens(hand, starter, total=15):
    """Return number of unique fifteen-pairs of a hand paired with a starter card
    WRITE UNIT TEST FOR THIS"""
    # include the starter card in the hand if recursion depth is 0
    if starter != -1:
        hand = [starter] + hand
        hand = map(card_value, hand)

    # base case
    if len(hand) == 1:
        if total == hand[0]:
            return 1
        else:
            return 0

    # recursively call fifteens() on the cases with and without using the first card
    else:
        return count_fifteens(hand[1:], -1, total-hand[0]) + count_fifteens(hand[1:], -1, total)


def count_run(hand, starter):
    """Return the length of the largest run of a hand paired with a starter card
    NOT COMPLETE"""
    # add the starter to the hand
    hand += [starter]
    hand = sorted(hand)

    return 0


def count_pairs(hand, starter):
    """Return number of pairs of a hand paired with a starter card
    WRITE UNIT TEST FOR THIS"""
    # add the starter to the hand
    hand += [starter]

    score = 0

    n = len(hand)
    for i in xrange(n-1):
        for j in xrange(i+1,n):
            if hand[i] == hand[j]:
                score += 1
    return score


def count_flush(hand, starter,crib=False):
    """Return the length of the largest flush (greater than 3) of a hand paired with a starter card"""
    return 0


def count_nobs(hand, starter):
    """Return 1 if a hand paired with a starter card contains nobs, 0 otherwise
    WRITE UNIT TEST FOR THIS"""
    for card in hand:
        if ranks[card_rank(card)] == 'J' and card_suite(card) == card(suite):
            return 1
    return 0

