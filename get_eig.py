import numpy as np

def get_eig(X):
    """
    Computes the eigenvalues and eigenvectors of X.
    :param X: numpy ndarray of size 2xN
    :return: sorted (descending) eigenvalues and eigenvectors of X
    """

    # Compute covariance matrix
    C = np.cov(X.T)
    # Compute eigenvalues
    eig_val, eig_vec = np.linalg.eig(C)
    # Sort eigenvalues in descending order
    idx = np.argsort(eig_val)[::-1]
    # Reorder eigenvalues and compute sqrt
    eig_val = np.sqrt(eig_val[idx])
    # Reorder eigenvectors
    eig_vec = eig_vec[:,idx]

    return eig_val, eig_vec