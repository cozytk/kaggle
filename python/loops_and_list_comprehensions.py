"""
1.

Have you ever felt debugging involved a bit of luck? The following program has a bug. Try to identify the bug and fix it.
"""

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
        else:
            return False


def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    return any([num % 7 == 0 for num in nums])


"""
2.

a.

Look at the Python expression below. What do you think we'll get when we run it? When you've made your prediction, uncomment the code and run the cell to see if you were right.
"""

[1, 2, 3, 4] > 2

"""
b

R and Python have some libraries (like numpy and pandas) compare each element of the list to 2 (i.e. do an 'element-wise' comparison) and give us a list of booleans like [False, False, True, True].

Implement a function that reproduces this behaviour, returning a list of booleans corresponding to whether the corresponding element is greater than n.
"""

def elementwise_greater_than(L, thresh):
    return [num > thresh for num in L]

"""
3.

Complete the body of the function below according to its docstring.
"""

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False



"""
4. 🌶️

Next to the Blackjack table, the Python Challenge Casino has a slot machine. You can get a result from the slot machine by calling play_slot_machine(). The number it returns is your winnings in dollars. Usually it returns 0. But sometimes you'll get lucky and get a big payday. Try running it below:

```python
play_slot_machine()
```
add Codeadd Markdown
By the way, did we mention that each play costs $1? Don't worry, we'll send you the bill later.

On average, how much money can you expect to gain (or lose) every time you play the machine? The casino keeps it a secret, but you can estimate the average value of each pull using a technique called the Monte Carlo method. To estimate the average outcome, we simulate the scenario many times, and return the average result.

Complete the following function to calculate the average value per play of the slot machine.
"""

def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    ret = 0
    for i in range(n_runs):
        ret = ret + play_slot_machine() - 1
        i + 1
    return ret / n_runs



