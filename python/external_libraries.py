"""

1.

After completing the exercises on lists and tuples, Jimmy noticed that, according to his estimate_average_slot_payout function, the slot machines at the Learn Python Casino are actually rigged against the house, and are profitable to play in the long run.

Starting with $200 in his pocket, Jimmy has played the slots 500 times, recording his new balance in a list after each spin. He used Python's matplotlib library to make a graph of his balance over time:
"""

# Import the jimmy_slots submodule
from learntools.python import jimmy_slots
# Call the get_graph() function to get Jimmy's graph
graph = jimmy_slots.get_graph()
graph.set_title("Results of 500 slot machine pulls")
graph.set_ylim(0)
graph


def prettify_graph(graph):
    """Modify the given graph according to Jimmy's requests: add a title, make the y-axis
    start at 0, label the y-axis. (And, if you're feeling ambitious, format the tick marks
    as dollar amounts using the "$" symbol.)
    """
    graph.set_title("Results of 500 slot machine pulls")
    graph.set_ylim(bottom = 0)
    graph.set_ylabel("Balance")
#     graph.set_yticks("$")

graph = jimmy_slots.get_graph()
prettify_graph(graph)
help(graph.set_yticklabels)



"""
2. 🌶️🌶️

This is a very hard problem. Feel free to skip it if you are short on time:

Luigi is trying to perform an analysis to determine the best items for winning races on the Mario Kart circuit. He has some data in the form of lists of dictionaries that look like...

[
    {'name': 'Peach', 'items': ['green shell', 'banana', 'green shell',], 'finish': 3},
    {'name': 'Bowser', 'items': ['green shell',], 'finish': 1},
    # Sometimes the racer's name wasn't recorded
    {'name': None, 'items': ['mushroom',], 'finish': 2},
    {'name': 'Toad', 'items': ['green shell', 'mushroom'], 'finish': 1},
]
'items' is a list of all the power-up items the racer picked up in that race, and 'finish' was their placement in the race (1 for first place, 3 for third, etc.).

He wrote the function below to take a list like this and return a dictionary mapping each item to how many times it was picked up by first-place finishers.
"""

def best_items(racers):
    """Given a list of racer dictionaries, return a dictionary mapping items to the number
    of times those items were picked up by racers who finished in first place.
    """
    winner_item_counts = {}
    for i in range(len(racers)):
        # The i'th racer dictionary
        racer = racers[i]
        # We're only interested in racers who finished in first
        if racer['finish'] == 1:
            for j in racer['items']:
                # Add one to the count for this item (adding it to the dict if necessary)
                if j not in winner_item_counts:
                    winner_item_counts[i] = 0
                winner_item_counts[i] += 1

        # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                i+1, len(racers), racer['name'])
                 )
    return winner_item_counts


"""
3. 🌶️

Suppose we wanted to create a new type to represent hands in blackjack. One thing we might want to do with this type is overload the comparison operators like > and <= so that we could use them to check whether one hand beats another. e.g. it'd be cool if we could do this:

>>> hand1 = BlackjackHand(['K', 'A'])
>>> hand2 = BlackjackHand(['7', '10', 'A'])
>>> hand1 > hand2
True
Well, we're not going to do all that in this question (defining custom classes is a bit beyond the scope of these lessons), but the code we're asking you to write in the function below is very similar to what we'd have to write if we were defining our own BlackjackHand class. (We'd put it in the __gt__ magic method to define our custom behaviour for >.)

Fill in the body of the blackjack_hand_greater_than function according to the docstring.
"""


def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.

    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21

    Hands are represented as a list of cards. Each card is represented by a string.

    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.

    When determining a hand's total, you should try to count aces in the way that
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.

    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    sum_hand_1 = 0
    a_hand_1 = 0
    sum_hand_2 = 0
    a_hand_2 = 0
    for num in hand_1:
        if num == 'J' or num == 'Q' or num == 'K':
            num = 10
        elif num == 'A':
            a_hand_1 += 1
            num = 0
        else:
            num = int(num)
        sum_hand_1 += num
    if a_hand_1:
        if sum_hand_1 + a_hand_1 + 10 <= 21:
            sum_hand_1 += a_hand_1 + 10
            a_hand_1 = 0
        else:
            sum_hand_1 += a_hand_1
    if sum_hand_1 > 21:
        return (False)
    for num in hand_2:
        if num == 'J' or num == 'Q' or num == 'K':
            num = 10
        elif num == 'A':
            a_hand_2 += 1
            num = 0
        else:
            num = int(num)
        sum_hand_2 += num
    if a_hand_2:
        if sum_hand_2 + a_hand_2 + 10 <= 21:
            sum_hand_2 += a_hand_2 + 10
            a_hand_2 = 0
        else:
            sum_hand_2 += a_hand_2
    if sum_hand_1 > sum_hand_2 or sum_hand_2 > 21:
        return (True)
    else:
        return False