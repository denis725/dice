from __future__ import division

import random

from app.utils import make_check
from app.utils import cancel
from app.utils import roll


def test_cancel():
    assert cancel(10, 2) == (5, 1)
    assert cancel(2, 10) == (1, 5)
    assert cancel(17411, 757) == (23, 1)
    assert cancel(12, 8) == (3, 2)
    assert cancel(13 * 17, 11 * 17) == (13, 11)
    for __ in range(10):
        x = random.randint(1, 100)
        assert cancel(1, x) == (1, x)
        assert cancel(0, x) == (0, x)


def test_make_check():
    # make_check(required_check, list_of_dice, added, strictly_greater)
    
    # prob to roll a 10 with a d10
    num_suc, num_tot, chance =  make_check(10, [10], 0, False)
    assert 1.0 * num_suc / num_tot == 0.01 * chance
    assert cancel(num_suc, num_tot) == (1, 10)
    
    # prob to roll > 10 with a d10
    num_suc, num_tot, chance =  make_check(10, [10], 0, True)
    assert cancel(num_suc, num_tot) == (0, 10)

    # prob to roll a 13 with 2 d6 and bonus 1
    num_suc, num_tot, chance =  make_check(13, [6, 6], 1, False)
    assert cancel(num_suc, num_tot) == (1, 36)

    # prob to roll an 11 with 2 d6 and bonus -1
    num_suc, num_tot, chance =  make_check(11, [6, 6], -1, False)
    assert cancel(num_suc, num_tot) == (1, 36)

    # prob to roll > 10 with 2 d6 and bonus -1
    num_suc, num_tot, chance =  make_check(10, [6, 6], -1, True)
    assert cancel(num_suc, num_tot) == (1, 36)

    # prob to roll a 11 with 2 d6
    num_suc, num_tot, chance =  make_check(11, [6, 6], 0, False)
    assert cancel(num_suc, num_tot) == cancel(3, 36)

    # prob to roll a 15 with a d10 and a d5
    num_suc, num_tot, chance =  make_check(15, [10, 5], 0, False)
    assert cancel(num_suc, num_tot) == (1, 50)

    # prob to roll a 14 with a d10 and a d5
    num_suc, num_tot, chance =  make_check(14, [10, 5], 0, False)
    assert cancel(num_suc, num_tot) == (3, 50)

    # prob to roll a 123 with a d100, a d17 and a d6
    num_suc, num_tot, chance =  make_check(123, [100, 17, 6], 0, False)
    assert cancel(num_suc, num_tot) == (1, 100 * 17 * 6)

    # prob to roll a 2 with a d10 and a d5
    num_suc, num_tot, chance =  make_check(2, [10, 5], 0, False)
    assert cancel(num_suc, num_tot) == (1, 1)

    # prob to roll a 1 with a d10 and a d5
    num_suc, num_tot, chance =  make_check(1, [10, 5], 0, False)
    assert cancel(num_suc, num_tot) == (1, 1)


def test_roll():
    # roll is like a simulation, so we can test it against the odds
    # to keep calculation time down, we don't make too many simulations
    # but allow some of the results to deviate from expectation

    lst1 = [5, 6, 7]
    diff = []
    for check1 in range(5, 15):
        __, __, chance =  make_check(check1, lst1, 0, False)
        simulation = [roll(lst1) >= check1 for ___ in range(100000)]
        diff.append(0.01 * chance - sum(simulation) / len(simulation))
    assert sum(map(lambda x: x < 1e-3, map(abs, diff))) <= 9

    lst1 = [4, 8, 12, 20]
    diff = []
    for check1 in range(15, 25):
        __, __, chance =  make_check(check1, lst1, 0, False)
        simulation = [roll(lst1) >= check1 for ___ in range(100000)]
        diff.append(0.01 * chance - sum(simulation) / len(simulation))
    assert sum(map(lambda x: x < 1e-3, map(abs, diff))) <= 9
