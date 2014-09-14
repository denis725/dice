from __future__ import division, print_function, absolute_import

import itertools as it
import random


def make_check(required_check, list_of_dice,
               added=0, strictly_greater=False):
    required_check -= added
    required_check += 1 if strictly_greater else 0
    gen = it.product(*tuple(range(1, eyes + 1) for eyes in list_of_dice))
    sums = sum([sum(tup) >= required_check for tup in gen])
    totals = reduce(lambda x, y: x * y, list_of_dice)
    sums, totals = cancel(sums, totals)
    return sums, totals, 100.0 * sums / totals


def cancel(x, y):
    """ Cancel x / y """
    maxi = min(x, y)
    i = 2
    while i <= maxi:
        if (x % i == 0) & (y % i == 0):
            x /= i
            y /= i
            maxi /= i
        else:
            i += 1
    return x, y


def roll(list_of_dice):
    rand_rolls = [random.randint(1, die) for
                  die in list_of_dice]
    return reduce(lambda x, y: x + y, rand_rolls)


def rolls(list_of_dice):
    rand_rolls = [random.randint(1, die) for
                  die in list_of_dice]
    return rand_rolls
