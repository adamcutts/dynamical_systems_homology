import numpy as np


def takens_embedding(s, d, T):
    # s is the time series under consideration
    # d is the delay embedding dimension (number of delays considered), an integer
    # T is the delay, an integer
    N = len(s)
    X = np.zeros((d, N - (d-1)*T))
    for i in range(d):
        X[i] = s[T*i:N - (d-1)*T + i*T:1]
    return X

