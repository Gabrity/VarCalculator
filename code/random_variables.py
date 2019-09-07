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


