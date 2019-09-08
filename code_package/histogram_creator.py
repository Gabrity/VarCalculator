"""Module responsible for plotting histograms"""
import matplotlib.pyplot as plt


def create_histogram(histogram_data):
    """Draws histogram for random sample with ~10.000.000 draws"""
    num_bins = 150
    plt.hist(histogram_data, num_bins, facecolor='black', alpha=1)
    plt.ylabel('Number of draws')
    plt.xlabel('Value of distribution')
    plt.show()
