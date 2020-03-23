import numpy as np

def l2_norm(a,b):
    """
    Computes L2 norm between two vectors
    :param a: Nxd numpy ndarray
    :param b: Nxd numpy ndarray
    :return: L2 nrom between vectors
    """

    if a.ndim == 1:
        return np.sqrt(np.sum((a-b)**2))
    else:
        return np.sqrt(np.sum((a-b)**2, axis=1))