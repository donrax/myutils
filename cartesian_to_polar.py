import numpy as np

def cartesian_to_polar(x, y):
    """
    Transforms cartesian coordinates to polar coordinates.
    :param x: 1D numpy ndarray of x coordinates
    :param y: 1D numpy ndarray of y coordinates
    :return: numpy ndarray of r values and thr values in radians
    """

    r = np.sqrt(x**2 + y**2)
    thr = np.arctan2(y,x)

    return r, thr