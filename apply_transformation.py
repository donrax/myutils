import warnings
import numpy as np

def apply_transformation(X, T):
    """
    Applies the 2D or 3D transformation matrix T to 2D or 3D data points in X.
    :param X: Nx2 or Nx3 numpy ndarray
    :param T: 3x3 (2D) or 4x4 (3D) numpy ndarray
    :return: Transformed points
    """

    # Check input
    #if X.shape[1] != 2L and X.shape[1] != 3L: # Python27
    if X.shape[1] != 2 and X.shape[1] != 3:
        warnings.warn("Input array must be of shape Nx2 or Nx3!")

    # Add homogeneus coordinate
    X = np.vstack([X.T, np.ones(X.shape[0])])
    # Transform points
    t_X = T.dot(X).T
    # Divide by homogeneus value
    t_X = np.asarray([row/row[-1] for row in t_X])

    # Return without homogeneus coordinate
    return t_X[:,0:-1]