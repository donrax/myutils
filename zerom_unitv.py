import sys

def zerom_unitv(X, dim=2):
    eps = sys.float_info.epsilon # For numerical stability
    if dim == 2:
        # Remove the average (zero-mean) and divide by std (unit-variance)
        X = (X-X.mean()) / (X.std()+eps)
        # Rescale back to 0-1
        X = X-X.min(); X = X / (X.max()+eps)
    elif dim == 3:
        # Remove the average (zero-mean) and divide by std (unit-variance)
        R = X[:,:,0]; R = (R-R.mean()) / (R.std()+eps)
        G = X[:,:,1]; G = (G-G.mean()) / (G.std()+eps)
        B = X[:,:,2]; B = (B-B.mean()) / (B.std()+eps)
        # Rescale back to 0-1
        R = R-R.min(); X[:,:,0] = R / (R.max()+eps)
        G = G-G.min(); X[:,:,1] = G / (G.max()+eps)
        B = B-B.min(); X[:,:,2] = B / (B.max()+eps)
    return X