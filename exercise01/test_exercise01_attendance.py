import unittest

import numpy as np

from exercise01_attendance import is_odd, sum_of_odds_builtins, sum_of_odds_while

print("Test attendance exercise 1\n" + 70 * "-")


class TestExercise01Attendance(unittest.TestCase):
    """
    Test attendance exercise 1.
    """

    def setUp(self):
        self.test_numbers = list(range(20))

    def test_is_odd_on_odd(self):
        "Test ``is_odd`` on odd numbers"
        for num in np.arange(start=-999, stop=999, step=2):
            self.assertEqual(is_odd(num), True)

    def test_is_odd_on_even(self):
        "Test ``is_odd`` on even numbers"
        for num in np.arange(start=-998, stop=998, step=2):
            self.assertEqual(is_odd(num), False)

    def test_sum_of_odds_while(self):
        "Test ``sum_of_odds_while``"
        for num in self.test_numbers:
            self.assertEqual(sum_of_odds_while(num), num**2)

    def test_sum_of_odds_builtins(self):
        "Test ``sum_of_odds_builtins``"
        for num in self.test_numbers:
            self.assertEqual(sum_of_odds_builtins(num), num**2)
