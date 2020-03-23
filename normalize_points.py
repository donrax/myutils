import warnings
import numpy as np
from myutils.apply_transformation import apply_transformation

def normalize_points( X ):
    """
    Normalizes 2D or 3D points using R. Hartley's pre-conditioning (R. I. Hartley, "In Defense of the Eight-Point Algorithm", PAMI 1997).
    :param X: Nx2 or Nx3 numpy ndarray
    :return: Normalized points and normalization matrix
    """

    # Check input 
	#if X.shape[1] != 2L and X.shape[1] != 3L: # Python27
    if X.shape[1] != 2 and X.shape[1] != 3:
        warnings.warn("Input array must be of shape Nx2 or Nx3!")

    # Center data: Translate center of mass to origin
    mu = np.mean(X, axis=0)
    X_tmp = X - mu

    # Scale data: Force average distance (Root Mean Square Error) of points from origin to sqrt(2)
    rmse = np.sqrt(np.sum(X_tmp**2, axis=1).mean())
    s = np.sqrt(2) / rmse

    # Construct normalization matrix
    T = np.array([[s, 0, -s*mu[0]], [0, s, -s*mu[1]], [0, 0, 1]])

    # Normalize points
    X_norm = apply_transformation(X, T)

    """
    plt.figure()
    plt.plot(X[:,0],X[:,1],'bo')
    plt.plot(X_norm[:,0],X_norm[:,1],'ro')
    xa = numpy.array([[-1, 0], [1, 0]])
    ya = numpy.array([[0, -1], [0, 1]])
    plt.plot(xa[:,0],xa[:,1],'k-')
    plt.plot(ya[:,0],ya[:,1],'k-')
    plt.axis('equal')
    plt.legend(['Initial','Normalized'])
    """

    return X_norm, T