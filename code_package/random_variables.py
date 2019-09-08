"""Module for generating random numbers and perform statistical calculations"""
import random
import math
import numpy as np


def calculate_nth_moment(sample, moment):
    """Calculate nth moment of a given sample"""
    sample_size = len(sample)
    if sample_size <= 0:
        raise ValueError("Sample size must be larger than 0:", sample_size)
    aggregate_sum = 0
    for item in sample:
        aggregate_sum = aggregate_sum + item ** moment
    return aggregate_sum / sample_size


def estimate_var(sample, threshold):
    """Calculates a certain var of a given sample"""
    sample_size = len(sample)
    index_at = get_var_level_index(sample_size, threshold)
    sample.sort()
    return sample[index_at]


def get_var_level_index(sample_size, threshold):
    """Helper method to calculate the index in a given sample which is at a certain percentile.
    Returned value is an index, rounded to the lower integer value giving a pessimistic estimation.
    No interpolation is used, a fixed index is chosen. Invalid thresholds are silently fixed."""
    if sample_size <= 0:
        raise ValueError("Sample size cannot be non-positive:", sample_size)
    if threshold <= 0.0:
        return 0
    if threshold >= 1.0:
        return sample_size - 1
    return int(math.floor(sample_size * threshold))


def estimate_cumulative_distribution(sample, threshold):
    """Statistical estimation for the probability that a random variable is smaller than a given
    threshold using sample of identically distributed random draws"""
    sample_size = len(sample)
    if sample_size == 0:
        raise ValueError("Sample cannot be empty when estimating cumulative distribution")
    count = 0
    for item in sample:
        if item <= threshold:
            count = count + 1
    return count / sample_size


def create_distribution(sample_size):
    """Generation of a vector of hybrid distribution"""
    if sample_size < 0:
        raise ValueError("Unable to generate negative number of distributions ", sample_size)
    result = []
    for _ in range(sample_size):
        result.append(get_hybrid_distribution())
    return result


def get_hybrid_distribution():
    """Combining the discrete and standard normal distributions"""
    return get_discrete_distribution() + get_standard_normal_distribution()


def get_discrete_distribution():
    """Generator for a specific discrete distribution"""
    random_int = random.randint(1, 4)
    if (random_int == 1) | (random_int == 2):
        return 0
    if random_int == 3:
        return 3
    if random_int == 4:
        return 5
    raise ValueError("Unable to generate discrete distribution with ", random_int)


def get_standard_normal_distribution():
    """Standard normal distribution generator"""
    return np.random.normal(0, 1)
