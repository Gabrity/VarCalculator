from unittest import TestCase
import random


def discrete_random_distribution():
    for x in range(10):
        x = random.randint(1, 4)
        if x == 1 | x == 2:
            y = 0
        if x == 3:
            y = 3
        if x == 4:
            y = 5
    return y


class TestRandomVariables(TestCase):
    def test_discrete_random_distribution(self):
        result = discrete_random_distribution()
        if result != 0 & result != 3 & result != 5:
            self.fail

