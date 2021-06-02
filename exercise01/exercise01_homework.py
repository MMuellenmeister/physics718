"""
Template for the homework of exercise sheet 01.

Remember to run the tests (just run the file) to see if your solution is
correct.
"""

import unittest

# if you want you can re-use the is_odd function from the attendance exercise
from exercise01_attendance import is_odd


# homework problem 1

def odd_fibonacci_numbers(n_numbers):
    """
    Return a list of the first N odd fibonacci numbers
    """
    if n_numbers == 1: return [1] 
    fib_list= [1,1]
    odd_fib_list = [1,1]
    while len(odd_fib_list)<n_numbers: 
        fib_list.append(fib_list[-1]+fib_list[-2])
        if fib_list[-1]%2==1:
            odd_fib_list.append(fib_list[-1])
    return odd_fib_list


# Optionally: Use a helper function that returns fibonacci numbers and use that
# in your main function that calculates the odd fibonacci numbers
def nth_fibonacci_number(number):
    """
    Helper function that return nth fibonacci number
    """
    pass


# homework problem 2

def sum_square_difference(numbers):
    """
    Return ∑(x_1²) - (∑x_n)²
    """
    return sum(i**2 for i in numbers)-sum(numbers)**2


def func_square_difference(func, numbers):
    """
    Return func(x_1²...x_n²) - func(x_1...x_n)²

    :param func: And aggregating function that takes a list and returns a scalar number.
    """
    return func([i**2 for i in numbers])-func(numbers)**2


def mean(numbers):
    "Calculates the arithmetic mean of ``numbers``"
    return sum(numbers)/len(numbers)


def variance(numbers):
    "Calculates the variance of ``numbers``"
    return func_square_difference(mean, numbers)


if __name__ == '__main__':
    unittest.main(module="test_exercise01_homework", verbosity=2)
