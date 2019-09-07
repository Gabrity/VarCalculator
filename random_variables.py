import random
import numpy as np


def create_distribution(sample_size):
    result = []
    for x in range(sample_size):
        result.append(get_hybrid_distribution())
    return result


def get_hybrid_distribution():
    return get_discrete_distribution() + get_standard_normal_distribution()


def get_discrete_distribution():
    x = random.randint(1, 4)
    if (x == 1) | (x == 2):
        return 0
    if x == 3:
        return 3
    if x == 4:
        return 5


def get_standard_normal_distribution():
    return np.random.normal(0, 1)






