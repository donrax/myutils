import numpy as np

def line_intersection_point(a1, a2, b1, b2):
    """
    Returns the intersection point between two lines.
    :param a1: [numpy ndarray] start of line segment
    :param a2: [numpy ndarray] end of line segment
    :param b1: [numpy ndarray] start of line segment
    :param b2: [numpy ndarray] end of line segment
    :return: intersection point between lines or [] if no intersection
    """

    # Get vector from a1 to a2
    v = a2 - a1
    # Get vector from b1 to b2
    w = b2 - b1

    # Check determinant if lines are parallel
    d = np.cross(v,w)
    if d == 0: return []

    # Compute intersection point
    q = ( (b1-b2)*np.cross(a1,a2) - (a1-a2)*np.cross(b1,b2) ) / d

    return q