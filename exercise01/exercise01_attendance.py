import unittest


def is_odd(num):
    "Returns ``True`` is n is odd."
    return bool(num%2)


def sum_of_odds_while(num_odds):
    """
    Calculate sum of first ``num_odds`` odd numbers from 1 updwards.
    """
    # raise and exception for negative inputs
    if num_odds < 0:
        raise ValueError("`num_odds` must be a positive number")
    # initialize numbers
    current_number = 0
    n_odds = 0  # number of odd numbers so far
    sum_of_odds = 0  # sum of odd numbers so far
    # TODO: uncomment complete the following code
    while n_odds<num_odds :
        if is_odd(current_number):
            sum_of_odds += current_number
            n_odds += 1
        current_number += 1
    return sum_of_odds


def sum_of_odds_builtins(num_odds):
    """
    Calculate sum of first ``num_odds`` odd numbers from 1 updwards via python
    builtin functions.
    """
    # raise and exception for negative inputs
    if num_odds < 0:
        raise ValueError("`num_odds` must be a positive number")
    # TODO: uncomment and complete the follwing code
    odds = range(1,num_odds*2, 2)
    sum_of_odds =  sum(odds)
    return sum_of_odds


def list_of_sum_of_odds(n):
    return [sum_of_odds_while(i) for i in range(n)]


if __name__ == "__main__":
    unittest.main(module="test_exercise01_attendance", verbosity=2)
