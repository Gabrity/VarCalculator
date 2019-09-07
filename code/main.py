import random


def main():
    for x in range(10):
        print
        random.randint(1, 101)


try:
    main()
# Naive assumption is that inputs are correct, and if not, ValueError exception is thrown. Incorrect inputs are not
# handled in a nice way for the sake of simplicity.
except ValueError as error:
    print('Caught this error: ' + repr(error))

