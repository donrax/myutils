import numpy as np

def polar_to_cartesian(r, thr):
    """
    Transforms polar coordinates to cartesian coordinates.
    :param r: 1D numpy ndarray of radius values
    :param thr: 1D numpy ndarray of theta values in radians
    :return: numpy ndarray of x and y coordinates
    """

    x = r * np.cos(thr)
    y = r * np.sin(thr)

    return x, y