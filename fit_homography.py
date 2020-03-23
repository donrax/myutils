import numpy as np
from myutils.normalize_points import normalize_points

def fit_homography(src, dst, weg=np.array([])):
    """
    Fits a projective transformation between two d-dimensional point sets. Enforces algebraic distance ||h||=1.
    :param src: Nxd numpy ndarray d-dimensional data points
    :param dst: Nxd numpy ndarray d-dimensional data points
    :param weg: relative weights of data points (Nx1 numpy ndarray)
    :return: transformation matrix T from src to dst
    """

    # -------------------------------
    # Normalize points
    # -------------------------------
    src, Ts = normalize_points(src)
    dst, Td = normalize_points(dst)

    # -------------------------------
    # Set parameters
    # -------------------------------
    # Get number of d-dimensional points
    n = len(src)
    # Check if weights are provided
    if not weg.any():
        weg = np.ones(n)

    # -------------------------------
    # Construct matrix [A|b]
    # -------------------------------
    A = np.zeros([2*n,9])
    W = np.zeros([2*n,2*n])
    for i in range(n):
        # Construct matrix A
        # ax = (x, y, 1, 0, 0, 0, -x'x, -x'y, -x')
        # ay = (0, 0, 0, x, y, 1, -y'x, -y'y, -y')
        A[i*2  ,:] = np.array([ src[i,0], src[i,1], 1, 0, 0, 0, -dst[i,0]*src[i,0], -dst[i,0]*src[i,1], -dst[i,0] ])
        A[i*2+1,:] = np.array([ 0, 0, 0, src[i,0], src[i,1], 1, -dst[i,1]*src[i,0], -dst[i,1]*src[i,1], -dst[i,1] ])
        # Construct diagonal weigh matrix
        W[i*2  ,i*2  ] = weg[i]
        W[i*2+1,i*2+1] = weg[i]

    # -------------------------------
    # Estimate solution x
    # -------------------------------
    # SVD decomposition of weighted matrix A
    _, _, V = np.linalg.svd((A.T.dot(W)).dot(A))
    # Last column vector corresponds to h
    H = np.reshape(V[8],(3,3))

    # -------------------------------
    # Denormalize homography (Td\H*Ts)
    # -------------------------------
    H, _, _, _ = np.linalg.lstsq(Td,H.dot(Ts))

    return H