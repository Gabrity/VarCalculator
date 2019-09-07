from random_variables import create_distribution
from histogram_creator import create_histogram


def main():
    sample_size = 10**5
    print('Generating random distribution')
    sample_vector = create_distribution(sample_size)
    print('Creating histogram of random sample')
    create_histogram(sample_vector)


try:
    main()
except ValueError as error:
    print('Caught this error: ' + repr(error))
