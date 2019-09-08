"""Executable entry point for Task 1"""
from code_package.random_variables import create_distribution, estimate_cumulative_distribution, \
    estimate_var, calculate_nth_moment
from code_package.histogram_creator import create_histogram


def director():
    """Director method for Task 1"""
    sample_size = 10**7
    print('Generating random distribution with a sample of:', sample_size)
    sample_vector = create_distribution(sample_size)
    print('Creating histogram of random sample')
    create_histogram(sample_vector)
    print('Estimating probability that random variable is less than -2')
    probability = estimate_cumulative_distribution(sample_vector, -2.0)
    print('Empirical probability that Z <= -2 is', probability)
    print('Calculating VaR at 5%')
    var = estimate_var(sample_vector, 0.05)
    print('VaR of Z at 5% is', var)
    print('Calculating normalized moments of Z')
    for n_th in range(3, 11):
        moment = calculate_nth_moment(sample_vector, n_th)
        print('n =', n_th, 'moment of variable Z is ', moment)


try:
    director()
except ValueError as error:
    print('Caught this error: ' + repr(error))
