import numpy as np
import matplotlib.pyplot as plt


def info_content(x):
    if x == 0:
        return 0
    else:
        result = -x * np.log2(x)
        return result


def entropy(array):
    # The sums argument allows us to compute entropy of an array with entry-sums not equal to 1.
    # This avoids a floating point error for large arrays with small values
    # See appended txt file for explanation
    sums = np.sum(array)
    f = np.vectorize(info_content)
    info_array = f(array)
    result = np.log2(sums) + (1/sums) * np.sum(info_array)
    return result


#  Function takes as input some (2, n)-array (a time series of 2 features
#  and length n) and a number of bins n_bin. It returns the mutual
#  information of the different features where the probability of some
#  features is proportional to the amount of observations in each bin.
#
#  We assume that every feature lies in some interval [x_min, x_max]
#
#  Returns mutual information in log base 2


def mutual_info(s, n_bin):
    #  s ------- a time series of shape (2, n)
    #  n_bin --- number of bins
    n = s.shape[1]
    x_min, x_max = [s.min(), s.max()]
    bins = np.linspace(x_min, x_max, n_bin+1)
    full_bins = np.tile(bins, (2, 1))  # Returns the bins over all dimensions
    frequency_map = np.histogramdd(s.T, bins=full_bins)[0]  # Returns the binned probability frequency map

    array_1 = np.sum(frequency_map, axis=0)
    array_2 = np.sum(frequency_map, axis=1)
    entropy_1 = entropy(array_1)
    entropy_2 = entropy(array_2)
    entropy_12 = entropy(frequency_map)
    result = entropy_1 + entropy_2 - entropy_12  # Uses standard formula for mutual information
    return result

