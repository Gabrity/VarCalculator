import matplotlib.pyplot as plt


def create_histogram(x):
    num_bins = 150
    plt.hist(x, num_bins, facecolor='black', alpha=1)
    plt.ylabel('Number of draws')
    plt.xlabel('Value of distribution')
    plt.show()

