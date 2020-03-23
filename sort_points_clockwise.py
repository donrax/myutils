import numpy as np
from myutils.cartesian_to_polar import cartesian_to_polar

def sort_points_clockwise(X):
    """
    Sorts points clockwise.
    :param X: Nx2 numpy ndarray
    :return: points sorted clockwise
    """

    # Center points
    mu = np.mean(X, axis=0)
    X = X - mu
    # Sort points
    _, thr = cartesian_to_polar(X[:,0], X[:,1])
    sidx = np.argsort(thr)
    X = X[sidx,:]
    # Translate points
    X = X + mu

    return X, sidx