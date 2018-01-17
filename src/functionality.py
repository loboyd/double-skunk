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
    NOT COMPLETED:
    things to count:
        - fifteen(s)
        - run(s)
        - pair(s)
        - flush
        - nobs
    """    
    return sum([fifteens(hand, starter),
                runs(hand, starter),
                pairs(hand, starter),
                flush(hand, starter),
                nobs(hand, starter)])


def fifteens(hand, starter, total=15):
    """Return fifteens-only score contribution of a hand paired with a starter card
    
    WRITE UNIT TEST FOR THIS"""
    # include the starter card in the hand if recursion depth is 0
    if starter != -1:
        hand = [starter] + hand
        hand = map(card_value, hand)
    
    # base case
    if len(hand) == 1:
        if total == hand[0]:
            return 2
        else:
            return 0
    
    # recursively call fifteens() on the cases with and without using the first card
    else:
        return fifteens(hand[1:], -1, total-hand[0]) + fifteens(hand[1:], -1, total)


def pairs(hand, starter):
    """Return pairs-only score contribution of a hand paired with a starter card
    
    WRITE UNIT TEST FOR THIS"""
    # add the starter to the hand
    hand += [starter]
    
    score = 0
    
    n = len(hand)
    for i in xrange(n-1):
        for j in xrange(i+1,n):
            if hand[i] == hand[j]:
                score += 2
    return score
    
