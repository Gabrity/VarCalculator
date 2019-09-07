import random


def main():
    for x in range(10):
        print(random.randint(1, 101))


try:
    main()
except ValueError as error:
    print('Caught this error: ' + repr(error))
